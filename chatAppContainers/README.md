This is a very basic demonstration of passing messages between containers. 
By running 'docker compose up --build' in the chatAppContainers directory, the containers build.
Then, by connecting to http://localhost:5000, the user is taken to a chat room.
Going to http://localhost:5001/messages, the user can see the messages that have been sent.

There are two containers set up for this connected through a network, app1 and app2. App1 is the interactable app, which is why it has a template html file. 
The html file has an internal JavaScript script to load messages on page refresh, so info is not lost on page refresh. 
The app.py inside app1 has code that communicates messages to app2, along with rendering the html file and some basic error checking. 
App2's python file handles recieving the message, and has no message sending capabilities, as it exists just to display messages sent to it.
Both containers have a Dockerfile which communicates with the top level compose.yaml file, and requirements.txt file to define what python libraries are necesary.
The compose.yaml file builds both containers, but importantly, connects them through a self defined network called chat-network, which uses a default driver.