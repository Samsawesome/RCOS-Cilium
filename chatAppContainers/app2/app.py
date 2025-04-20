from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Store messages in a list (in-memory for simplicity)
local_messages = []
messages = []
error_messages = []

# Serve the chat room UI
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint to get messages
@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

@app.route('/local_messages', methods=['GET'])
def get_local_messages():
    return jsonify(local_messages)

# Endpoint to send a message to Container 1
@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    message = data.get("message")
    sender_id = data.get("sender_id")  # Track sender to avoid infinite loop
    
    if message:
        if sender_id == 'app2':
            local_messages.append(message)  # Add the message to local container
            # Send the message to the other container (App2) with a sender ID of 'app1'
            requests.post("http://app3:5002/send_message", json={"message": message, "sender_id": "app2"})
            return (jsonify({"status": "Message sent successfully"}), 200)
        elif sender_id == 'app1':
            # If the sender is 'app2', prevent adding the message again in app1
            #if message not in local_messages:  # Check if the message is already in local messages
            messages.append(message)  # Add the message to local container
            return (jsonify({"status": "Message received from App2"}), 200)
        else:
            return (jsonify({"status": "Invalid sender"}), 400)
    else:
        return (jsonify({"status": "Message missing"}), 400)


@app.route('/admin_message', methods=['GET'])
def admin_message():
    if(len(local_messages) == 0):
        return "No dangerous messages sent yet."
    else:
      error_messages.append(local_messages.pop())
      return "Dangerous messages sent by user = " + str(len(error_messages))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
