from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Secure way: API key env var me rakho
API_KEY = os.getenv("SMM_API_KEY", "32b3d02ce682fac87c1cd2fc5455e48b")
API_URL = os.getenv("SMM_API_URL", "https://biggestsmmpanel.com/api/v2")

@app.route("/")
def home():
    return "✅ Flask Order API Running on Railway"

@app.route("/order/api/", methods=["GET"])
def order_api():
    video = request.args.get("video")
    service = request.args.get("service")
    quantity = request.args.get("quantity")

    if not video or not service or not quantity:
        return jsonify({"error": "Missing parameters: video, service, quantity"}), 400

    payload = {
        "key": API_KEY,
        "action": "add",
        "service": service,
        "link": video,
        "quantity": quantity,
    }

    try:
        r = requests.post(API_URL, data=payload, timeout=15)
        data = r.json()
    except Exception as e:
        return jsonify({"error": str(e)}), 502

    if r.ok and "order" in data:
        return jsonify({
            "message": "✅ Order placed successfully!",
            "order_id": data["order"]
        }), 200

    return jsonify({
        "error": data.get("error", "Unknown error"),
        "status_code": r.status_code
    }), 502

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
