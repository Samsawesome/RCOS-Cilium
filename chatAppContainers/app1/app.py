from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

#Store messages in a list
messages = []

# Serve the chat room UI
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint to get messages
@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

# Endpoint to send a message to Container 2
@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    message = data.get("message")
    
    if message:
        # Add message to local container messages
        messages.append(message)

        # Send the message to the other container (App2)
        requests.post("http://app2:5001/send_message", json={"message": message})
        
        return jsonify({"status": "Message sent successfully"}), 200
    else:
        return jsonify({"status": "Message missing"}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
