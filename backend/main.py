from datetime import datetime, timedelta
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from fastapi.security import APIKeyHeader
from dotenv import load_dotenv
import os

from backend.elastic import es
from backend.data import logs

load_dotenv("backend/.env")

app = FastAPI()

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

    total_logs = len(logs)

    high = 0
    medium = 0
    low = 0
    failed_logins = 0
    port_scans = 0
    suspicious = 0

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
            "failed_logins": failed_logins,
            "port_scans": port_scans,
            "suspicious_events": suspicious
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
        query={"match_all": {}}
    )

    logs = []

    for hit in response["hits"]["hits"]:
        logs.append(hit["_source"])

    return {
        "status": "success",
        "logs": logs
    }