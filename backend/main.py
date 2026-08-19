from datetime import datetime, timedelta
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from fastapi.security import APIKeyHeader
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
import os

from backend.elastic import es
from backend.correlation import correlate_events

load_dotenv("backend/.env")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

API_KEY = os.getenv("API_KEY")

api_key_header = APIKeyHeader(name="X-API-Key")


def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        return False

    return True


class Log(BaseModel):
    source: str
    event: str


# Automatic severity detection
def detect_severity(event: str):

    event = event.lower()

    if "port scan" in event:
        return "HIGH"

    elif "suspicious" in event:
        return "HIGH"

    elif "failed login" in event:
        return "MEDIUM"

    elif "login successful" in event:
        return "LOW"
    elif (
        "system health" in event
        or "routine" in event
        or "system check" in event
        or "health check" in event
        or "heartbeat" in event
        or "service running" in event
        or "service started" in event
        or "service stopped" in event
        or "system started" in event
        or "system shutdown" in event
        or "backup completed" in event
        or "update completed" in event
        or "configuration updated" in event
        or "connection established" in event
        or "monitoring active" in event
    ):
        return "INFO"

    else:
        return "LOW"

@app.get("/dashboard")
def dashboard(
    api_key: bool = Depends(verify_api_key)
):

    if not api_key:
        return {
            "message": "Invalid API Key"
        }
    response = es.search(
        index="logs",
        size=1000,
        query={"match_all": {}}
    )
    logs =[hit["_source"] for hit in response["hits"]["hits"]]
    incidents = correlate_events(logs)

    total_logs = len(logs)

    high = 0
    medium = 0
    low = 0
    info=0
    failed_logins = 0
    port_scans = 0
    suspicious = 0

    # NEW: Incident statistics
    total_incidents = len(incidents)
    high_risk_incidents = 0

    # NEW: Count high-risk incidents
    for incident in incidents:
        if incident["risk_score"] >= 70:
            high_risk_incidents += 1
    for log in logs:
        if "severity" not in log or "event" not in log:
            continue
        severity = log["severity"].lower()
        event = log["event"].lower()

        if severity == "high":
            high += 1
        elif severity == "medium":
            medium += 1
        elif severity == "low":
            low += 1
        elif severity == "info":
            info += 1

        if "failed login" in event:
            failed_logins += 1

        if "port scan" in event:
            port_scans += 1

        if "suspicious" in event:
            suspicious += 1

    return {
        "status": "success",
        "dashboard": {
            "total_logs": total_logs,
            "high_severity": high,
            "medium_severity": medium,
            "low_severity": low,
            "info_severity": info,
            "failed_logins": failed_logins,
            "port_scans": port_scans,
            "suspicious_events": suspicious,
            "total_incidents": total_incidents,
            "high_risk_incidents": high_risk_incidents
        }
    }

@app.post("/logs")
def add_log(
    log: Log,
    api_key: bool = Depends(verify_api_key)
):

    if not api_key:
        return {
            "message": "Invalid API Key"
        }

    # Automatically detect severity
    severity = detect_severity(log.event)

    new_log = {
    "source": log.source,
    "event": log.event,
    "severity": severity,
    "timestamp": datetime.now().isoformat()
}

    es.index(
    index="logs",
    document=new_log
)

    return {
    "status": "success",
    "message": "Log added successfully",
    "log": new_log
}

@app.get("/logs")
def get_logs(api_key: bool = Depends(verify_api_key)):

    if not api_key:
        return {"message": "Invalid API Key"}

    response = es.search(
        index="logs",
        size=50,
        query={"match_all": {}},
        sort=[
            {"timestamp": {"order": "desc",
                           "unmapped_type": "date"
                }}
        ]
    )

    logs = []

    for hit in response["hits"]["hits"]:
        logs.append(hit["_source"])

    return {
        "status": "success",
        "logs": logs
    }
@app.get("/incidents")
def get_incidents(
    api_key: bool = Depends(verify_api_key)
):

    if not api_key:
        return {
            "message": "Invalid API Key"
        }

    # Get logs from Elasticsearch
    response = es.search(
        index="logs",
        size=1000,
        query={"match_all": {}}
    )

    logs = []

    for hit in response["hits"]["hits"]:
        logs.append(hit["_source"])

    # Correlate related events
    incidents = correlate_events(logs)

    return {
        "status": "success",
        "incident_count": len(incidents),
        "incidents": incidents
    }