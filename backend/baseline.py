from collections import defaultdict
from datetime import datetime, timedelta


# ==========================================================
# RULE SETTINGS
# ==========================================================

# More than 5 failed logins within 1 minute = ALERT
FAILED_LOGIN_THRESHOLD = 5

TIME_WINDOW = timedelta(minutes=1)


# ==========================================================
# RULE-BASED DETECTOR
# ==========================================================

def rule_based_detection(logs):

    alerts = []

    failed_logins = []

    for log in logs:

        # ==================================================
        # YOUR ELASTICSEARCH FIELD
        # Your documents contain {"log": "..."}
        # ==================================================

        log_message = str(log.get("log", ""))


        # ==================================================
        # Extract timestamp
        # Example:
        # 2026-07-30 10:30:03 WARNING Multiple failed logins
        # ==================================================

        try:
            timestamp_string = log_message[:19]

            timestamp = datetime.strptime(
                timestamp_string,
                "%Y-%m-%d %H:%M:%S"
            )

        except ValueError:
            continue


        # ==================================================
        # RULE 1: Multiple failed logins
        # ==================================================

        if "failed login" in log_message.lower():

            failed_logins.append(timestamp)


    # ======================================================
    # Check whether >5 failed logins occurred within 1 minute
    # ======================================================

    failed_logins.sort()

    for i in range(len(failed_logins)):

        window_start = failed_logins[i]

        window_end = window_start + TIME_WINDOW

        count = sum(
            1
            for timestamp in failed_logins
            if window_start <= timestamp <= window_end
        )

        if count > FAILED_LOGIN_THRESHOLD:

            alerts.append({
                "rule": "Multiple Failed Logins",
                "count": count,
                "threshold": FAILED_LOGIN_THRESHOLD,
                "result": "ALERT"
            })

            break


    return alerts