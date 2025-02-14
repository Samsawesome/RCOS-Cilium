from flask import Flask, request, jsonify

app = Flask(__name__)

# Store messages in a list (in-memory for simplicity)
messages = []

# Endpoint to get messages
@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

# Endpoint to send a message to Container 1
@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    message = data.get("message")
    
    if message:
        # Add message to local container messages
        messages.append(message)
        return jsonify({"status": "Message received successfully"}), 200
    else:
        return jsonify({"status": "Message missing"}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
