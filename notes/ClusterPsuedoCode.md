The goal for this week (2/3 - 2/7) is to simulate and localhost a cluster network on my laptop. This will be done to eventually simulate network policies on top of the cluster, that will monitor and give permissions to traffic between nodes.
2/4 - 
After doing research, I have decidede that Docker is the best tool to use as a development and simulation tool. 
I downloaded Docker Desktop (off of the official Docker website) and I performed tutorials (through the application) to learn how to create and run containers.

Below are my personal notes:
Every Docker project contains a Dockerfile which acts as a sort of main file for the project.
You can run your Dockerfile with a command such as "docker build -t welcome-to-docker ."
docker tells the computer its a docker command, build tells docker to run the dockerfile, -t is a flag that indicates the next entry is a name, and the next entry is the name. This name is necesary because in the Dockerfile an image is created, and this name becomes the name of the image . Finally, the '.' is used to tell Docker the Dockerfile is in the current directory. 
When I say that Docker creates an image, I don't mean an .png or .jpg image, i mean a container that acts as a localhosted server.

Summary:
As of today, I have installed a container simulation software, and have learned the basics of the software.
Specifically, I have learned how to create containers using a Dockerfile, and how to use other people's create containers. 

2/7 - 
Today the goal is to get multiple containers to interact with each other. I am going to do this by continuing to do
tutorials through Docker.

Personal Notes:
So far I have been launching one container at a time, but the goal is to have multiple containers interacting, so launching one at 
a time is inefficient. Docker supports this with a tool called Docker Compose. It uses a .yaml file (same file typed used for network
security protocals) to launch multiple containers at once. The command run this time is 'docker compose up -d', where this command
runs everything in the .yaml files (which is titled compose.yaml), and the -d runs it in detached mode. It also taught the command
'docker compose watch', which allows you to make edits to files in real time and see them without having to recompose the files manually.
Unfortunently, the rest of the Docker tutorials are not helpful for this project, so I must now start reading through documentation.
I chose to read through the Docker Compose documentation as it is the tool that lets multiple containers exist at once (and more importantly,
interact with each other). 
There are three main components of a container. #1 is some sort of content (HTML, .py, etc). #2 is a Dockerfile, and #3 is a .yaml file.
Without #1, there will be nothing to host as a container. Without #2, Docker will not run (and therefore the container will not host), and
without #3, the container will run, but on fully default settings, which is unideal. The commands 'docker image ls' will list all the images
that the container is using, and running 'docker inspect <IMAGE ID>' will show the code of the image.

Summary:
I finished the relevent Docker tutorials, and have now started reading through documentation in order to better understand how I will impliment
a cluser of containers that all interact with each other. 