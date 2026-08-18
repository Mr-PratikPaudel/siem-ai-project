from datetime import datetime, timedelta


# Correlation settings
CORRELATION_WINDOW_MINUTES = 5
MIN_EVENTS_FOR_CORRELATION = 2


# Risk score assigned to each severity
SEVERITY_SCORES = {
    "LOW": 25,
    "MEDIUM": 50,
    "HIGH": 75,
    "CRITICAL": 100
}


def parse_timestamp(timestamp):
    """
    Convert an ISO timestamp string into a Python datetime object.
    """

    return datetime.fromisoformat(timestamp)


def calculate_risk_score(events):
    """
    Calculate the risk score of a group of related events.
    """

    scores = []

    for event in events:

        severity = event.get(
            "severity",
            "LOW"
        ).upper()

        score = SEVERITY_SCORES.get(
            severity,
            25
        )

        scores.append(score)

    if not scores:
        return 0

    # Average event risk
    average_score = sum(scores) / len(scores)

    # Increase risk when multiple related events occur
    event_bonus = min(
        len(events) * 5,
        20
    )

    final_score = average_score + event_bonus

    # Maximum score is 100
    final_score = min(
        round(final_score),
        100
    )

    return final_score


def determine_incident_severity(risk_score):
    """
    Convert numerical risk score into final incident severity.
    """

    if risk_score >= 90:
        return "CRITICAL"

    elif risk_score >= 70:
        return "HIGH"

    elif risk_score >= 40:
        return "MEDIUM"

    else:
        return "LOW"


def correlate_events(logs):
    """
    Group related security events based on:

    1. Same source
    2. Events occurring within the correlation time window
    """

    # Group logs by source
    grouped_logs = {}

    for log in logs:

        source = log.get("source")

        # Ignore logs that don't contain a source
        if not source:
            continue

        # Ignore logs without required correlation fields
        if not log.get("timestamp"):
            continue

        if source not in grouped_logs:
            grouped_logs[source] = []

        grouped_logs[source].append(log)

    incidents = []

    # Process each source separately
    for source, source_logs in grouped_logs.items():

        # Sort events by timestamp
        source_logs.sort(
            key=lambda log: parse_timestamp(
                log["timestamp"]
            )
        )

        current_group = []

        for log in source_logs:

            if not current_group:

                current_group.append(log)

                continue

            previous_time = parse_timestamp(
                current_group[-1]["timestamp"]
            )

            current_time = parse_timestamp(
                log["timestamp"]
            )

            time_difference = (
                current_time - previous_time
            )

            if time_difference <= timedelta(
                minutes=CORRELATION_WINDOW_MINUTES
            ):

                current_group.append(log)

            else:

                if len(current_group) >= MIN_EVENTS_FOR_CORRELATION:

                    incidents.append(
                        create_incident(
                            source,
                            current_group
                        )
                    )

                current_group = [log]

        # Process final group
        if len(current_group) >= MIN_EVENTS_FOR_CORRELATION:

            incidents.append(
                create_incident(
                    source,
                    current_group
                )
            )

    return incidents


def create_incident(source, events):
    """
    Create a correlated security incident.
    """

    # Calculate numerical risk
    risk_score = calculate_risk_score(
        events
    )

    # Convert risk score into severity
    severity = determine_incident_severity(
        risk_score
    )

    return {

        "source": source,

        "event_count": len(events),

        "risk_score": risk_score,

        "severity": severity,

        "start_time": events[0]["timestamp"],

        "end_time": events[-1]["timestamp"],

        "events": events
    }