from baseline import rule_based_detection
from elasticsearch import Elasticsearch


# Connect to Elasticsearch
es = Elasticsearch("http://localhost:9200")


# Get logs from Elasticsearch
response = es.search(
    index="logs",
    query={
        "match_all": {}
    },
    size=1000
)


# Extract log documents
logs = [
    hit["_source"]
    for hit in response["hits"]["hits"]
]


print("Total logs:", len(logs))


# Run baseline
alerts = rule_based_detection(logs)


print("\nRule-based alerts:")

if alerts:
    for alert in alerts:
        print(alert)
else:
    print("No alerts detected.")