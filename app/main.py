from fastapi import FastAPI
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response
import time
import random

app = FastAPI()

REQUEST_COUNT = Counter("http_requests_total", "Total HTTP requests", ["method", "endpoint"])
REQUEST_LATENCY = Histogram("http_request_duration_seconds", "Request latency", ["endpoint"])

@app.get("/")
def read_root():
    start_time = time.time()
    time.sleep(random.uniform(0.1, 0.5))
    duration = time.time() - start_time

    REQUEST_COUNT.labels(method="GET", endpoint="/").inc()
    REQUEST_LATENCY.labels(endpoint="/").observe(duration)
    
    return {"message": "Olá turma SENAC"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
