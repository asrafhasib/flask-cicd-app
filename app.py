from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "application": "Flask CI/CD Demo",
        "status": "Running",
        "version": os.getenv("APP_VERSION", "local"),
        "environment": os.getenv("APP_ENV", "development"),
    })

@app.get("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.get("/ready")
def ready():
    return jsonify({"status": "ready"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
