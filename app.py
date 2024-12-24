from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    if data["category"] == "card_payment.created":
        payment_details = data["data"]["attributes"]
        card_details = payment_details.get("card", {})
        print(f"Payment detected: Card {card_details.get('last_four')}, Amount: {payment_details.get('amount')} cents")
    return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

