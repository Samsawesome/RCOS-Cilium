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
