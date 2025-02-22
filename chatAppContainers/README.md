This is a very basic demonstration of passing messages between containers. 
By running 'docker compose up --build' in the chatAppContainers directory, the containers build.
Then, by connecting to http://localhost:5000, the user is taken to a chat room.
Going to http://localhost:5001, the user can see a complimentary chat room.
Sending messages in chat room 1 (5000), will make them appear in http://localhost:5000/local_messages,
as well as http://localhost:5001/messages. Sending messages from chat room 2 (5001) makes them appear
in the opposite directories. Local messages show up with a light blue background, and recieved
messages show up with a light green background. They are not displayed in order recieved, since I
only wanted to show messages being passed inbetween, and that has been shown.

There are two containers set up for this connected through a network, app1 and app2.  
The html files has an internal JavaScript script to load local messages on page refresh, so info is not lost on page refresh. 
The app.py files communicate between apps, along with rendering the html file and some basic error checking. 
Both containers have a Dockerfile which communicates with the top level compose.yaml file, and requirements.txt file to define what python libraries are necesary.
The compose.yaml file builds both containers, but importantly, connects them through a self defined network called chat-network, which uses a default driver.