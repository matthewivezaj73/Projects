from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "service": "store-backend",
        "status": "running",
        "store_id": os.getenv("STORE_ID", "unknown")
    }

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
