from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

#Store messages in a list
messages = []
sender = []


# Endpoint to get messages
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/messages')
def get_messages():
   combined_data = []
   for i in range(len(messages)):
      combined_data.append(messages[i]+", "+sender[i])
   return jsonify(combined_data) 


# Endpoint to send a message to Container 2
@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    message = data.get("message")
    sender_id = data.get("sender_id")  # Track sender to avoid infinite loop

    if message:
        messages.append(message)
        sender.append(sender_id)
        if "hacking" in message or "virus" in message or "hacker" in message:
            #if "dangerous" message sent
            if sender_id == 'app1': #tell sender they sent an invalid message, also dont send to other user
                requests.post("http://app1:5000/admin_message", json={"message": "ERROR DANGEROUS MESSAGE SENT"})
            elif sender_id == 'app2':
                requests.post("http://app2:5001/admin_message", json={"message": "ERROR DANGEROUS MESSAGE SENT"})
      
        elif sender_id == 'app1':
            # Send the message to the other container (App2) with a sender ID of 'app1'
            requests.post("http://app2:5001/send_message", json={"message": message, "sender_id": "app1"})
            return jsonify({"status": "Message sent successfully"}), 200
        elif sender_id == 'app2':
            # Send the message to the other container (App2) with a sender ID of 'app1'
            requests.post("http://app1:5000/send_message", json={"message": message, "sender_id": "app2"})
            return jsonify({"status": "Message sent successfully"}), 200
        else:
            return jsonify({"status": "Invalid sender"}), 400
    else:
        return jsonify({"status": "Message missing"}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
