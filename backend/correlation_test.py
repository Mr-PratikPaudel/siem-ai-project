from backend.correlation import correlate_events


test_logs = [
    {
        "source": "192.168.1.50",
        "event": "Failed login",
        "severity": "MEDIUM",
        "timestamp": "2026-08-17T10:00:00"
    },
    {
        "source": "192.168.1.50",
        "event": "Failed login",
        "severity": "MEDIUM",
        "timestamp": "2026-08-17T10:01:00"
    },
    {
        "source": "192.168.1.50",
        "event": "Port scan",
        "severity": "HIGH",
        "timestamp": "2026-08-17T10:03:00"
    },
    {
        "source": "192.168.1.20",
        "event": "Login successful",
        "severity": "LOW",
        "timestamp": "2026-08-17T10:02:00"
    }
]


incidents = correlate_events(test_logs)


print("Number of correlated incidents:", len(incidents))

for incident in incidents:
    print("\n--- CORRELATED INCIDENT ---")
    print("Source:", incident["source"])
    print("Events:", incident["event_count"])
    print("Risk Score:", incident["risk_score"])
    print("Severity:", incident["severity"])
    print("Start:", incident["start_time"])
    print("End:", incident["end_time"])

    print("Event chain:")

    for event in incident["events"]:
        print(
            "  -",
            event["timestamp"],
            "|",
            event["event"],
            "|",
            event["severity"]
        )