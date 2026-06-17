from fastapi import FastAPI
import os
import socket
from datetime import datetime

app = FastAPI(title="SRE Demo API")

APP_VERSION = os.getenv("APP_VERSION", "v1")
ENVIRONMENT = os.getenv("ENVIRONMENT", "local-argo-demo")

@app.get("/")
def root():
    return {
        "service": "sre-demo-api",
        "message": "Argo CD SRE demo application is running",
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
        "hostname": socket.gethostname()
    }

@app.get("/healthz")
def healthz():
    return {
        "status": "healthy",
        "version": APP_VERSION
    }

@app.get("/readyz")
def readyz():
    return {
        "status": "ready",
        "version": APP_VERSION
    }

@app.get("/version")
def version():
    return {
        "service": "sre-demo-api",
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
        "timestamp": datetime.utcnow().isoformat()
    }

@app.get("/api/orders/status")
def order_status():
    return {
        "orderService": "available",
        "processingStatus": "normal",
        "version": APP_VERSION
    }
