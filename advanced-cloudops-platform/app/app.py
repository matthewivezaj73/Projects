from flask import Flask, request
from prometheus_client import Counter, Histogram, generate_latest
import time

app = Flask(__name__)

REQUEST_COUNT = Counter(
    'app_requests_total',
    'Total App HTTP Requests',
    ['method', 'endpoint', 'http_status']
)

REQUEST_LATENCY = Histogram(
    'app_request_latency_seconds',
    'Request latency'
)

@app.route("/")
@REQUEST_LATENCY.time()
def home():
    REQUEST_COUNT.labels('GET', '/', '200').inc()
    return "CloudOps Platform Running"

@app.route("/error")
def error():
    REQUEST_COUNT.labels('GET', '/error', '500').inc()
    return "Internal Error", 500

@app.route("/metrics")
def metrics():
    return generate_latest()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
