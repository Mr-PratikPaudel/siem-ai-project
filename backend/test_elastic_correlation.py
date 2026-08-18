from backend.elastic import es
from backend.correlation import correlate_events


def get_logs_from_elasticsearch():

    response = es.search(
        index="logs",
        size=1000,
        query={"match_all": {}}
    )

    logs = []

    for hit in response["hits"]["hits"]:
        logs.append(hit["_source"])

    return logs


logs = get_logs_from_elasticsearch()

print("Total logs retrieved:", len(logs))


incidents = correlate_events(logs)

print("Correlated incidents found:", len(incidents))


for number, incident in enumerate(incidents, start=1):

    print("\n==============================")
    print("INCIDENT", number)
    print("==============================")

    print("Source:", incident["source"])
    print("Event count:", incident["event_count"])
    print("Severity:", incident["severity"])
    print("Risk Score:", incident["risk_score"])
    print("Start:", incident["start_time"])
    print("End:", incident["end_time"])

    print("\nEvent chain:")

    for event in incident["events"]:

        print(
            "  -",
            event["timestamp"],
            "|",
            event["event"],
            "|",
            event["severity"]
        )