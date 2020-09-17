# docker-compose-app
Docker compose practice to build an environment with reverse proxy on nginx, python flask app, redis and serving static content. 

## Installation
Clone the repository. And move to the root folder. Run the docker compose command as a deamon to start the project. 
```bash
docker-compose up -d
```
## Usage

After running the docker compose command the project will be expose at port 80 of your local machine. You can change the port configuration at the docker compose file. There are two possible routes in the project: 
localhost/static
localhost/app

## Python Flask Reminder App

You can change the behaviour of your python app just by modifying the app.py file. There are three available routes right now. Index to get the instructions of the app and /remember/[key]/[message] to save a custom message into the redis database. To get the message you can use the key with /message/[key]. 

## Static Content

To access the static content you can use the route localhost/static. It is a simple website made with bootstrap and served with nginx as static content in port 80. 

## Docker-Compose 

The docker compose set 4 different services: 
  - proxy: Here are the configurations for the proxy file. It depends on static and app to get built. 
  - app: Here is the configuration of the python app. It uses a volume to the /app directory. You can change the behaviour of the app and then restart the container to see the changes. 
  - redis: It grabs a redis image from dockerhub repository. 
  - static: Here is served the static content. It uses a volume to /static directory. 
 
 
