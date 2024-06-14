---
title: Docker
description: Docker, Docker Composer, Yml, Deployment
date: 05-11-2024
status: published
priority: 997
---

## Table of contents

## Images

### Base Image:

```Dockerfile
FROM node:22-alpine3.18
```

commands:

```bash
docker build -t react-app . # build image: docker client sends the content of the directory to docker engine
docker run -it react-app # interactive react app
docker run -it react-app sh # open a shell session inside the container
```

### Copying application files & directories

```Dockerfile
FROM node:22-alpine3.18
WORKDIR /app
COPY . .
# ADD https:....com .
# ADD file.zip . # Uncompressed the copressed file
```

### Excluding files & directories

```bash
# .dockerignore
node_modules/
```

### Running commands

```dockerfile
FROM node:22-alpine3.18
WORKDIR /app
COPY . .
RUN npm install
```

### Setting environment variables

```dockerfile
# ...
ENV API_URL=http:api.example.com
```

inspect env variable:

```bash
docker run -it react-app sh
printenv # print all env
printenv API_URL # print the API_URL env
echo $API_URL # print the API_URL env
```

### Exposing PORTs

EXPOSE command desn't automatically publish the port on the host.

```dockerfile
# ...
EXPOSE 3000
```

### Managing users in linux

```bash
useradd -m john # add user
cat /etc/passwd # print users
# john:x:1001:1001::/home/john:/bin/sh
# john is user
# x means password is stored someone else
# 1001 is the user id
# 1001 is the group id
# /home/john is home dir of john
# /bin/sh is the shell program

usermod -s /bin/bash john  # john:x:1001:1001::/home/john:/bin/bash

# password
cat /etc/shadow # john:!:19852:0:99999:7:::

# Login as john
docker exec -it -u john f227025e812b bash

# delete
userdel john

# latest version of useradd
adduser bob

addgroup app
adduser -S -G app app
groups app # app

addgroup md && adduser -S -G md md
```

### Setting the users

When you use USER app in a Dockerfile, it only sets the user for subsequent RUN, CMD, and ENTRYPOINT commands, not for COPY commands. The COPY command operates at the filesystem level within the Docker image and does not inherit the user set by USER.

```dockerfile
# ---
RUN addgroup app && adduser -S -G app app
USER app
```

```bash
/app $ whoami
app
```

### Entrypoints

```dockerfile
FROM node:14.16.0-alpine3.13
RUN addgroup app && adduser -S -G app app
USER app
WORKDIR /app
COPY . .
RUN npm install
ENV API_URL=http:api.example.com
EXPOSE 3000
CMD ["npm", "start"]
```

### Speeding up builds

An image is a collections of layers that only includes modified files. Once a layer is rebuilt, all the following layers have to be rebuilt. Put instructions that change a lot at the bottom, and instructions that don't change much at the top.

```dockerfile
FROM node:14.16.0-alpine3.13
RUN addgroup app && adduser -S -G app app
USER app
WORKDIR /app
COPY package*.json .
RUN npm install
COPY . .
ENV API_URL=http:api.example.com
EXPOSE 3000
CMD ["npm", "start"]
```

### Removing images and containers

```bash
docker image prune # This will remove all dangling images.
docker container prune # This will remove all stopped containers.
docker rmi image-name
docker image remove image-name:tag
docker rm container-name
```

### Tagging images

```bash
docker build -t react-app:1.1 .
docker image tag react-app:latest react-app:1.1
```

### Sharing Images

```bash
docker login # authenticate with your Docker Hub account.
docker tag [image_id] [username/repository_name] #Tag the image you want to share with your Docker Hub username and repository name.
docker push [username/repository_name] # upload your tagged image to Docker Hub.
```

### Saving & Loading an Image

```bash
docker save -o image.tar image_name:tag
docker load -i image.tar
```

## Containers

### Starting containers

```bash
docker ps # to see running containers. containers are special kind of processes (ps)
docker run -d --name demo-app react-app # -d Run container in background; --name  Assign a name to the container
```

### Viewing logs

```bash
docker logs -f demo-app # Follow log outpu
# -n Number of lines to show from the end of the logs
# -t Show timestamps
```

### Publishing ports

```bash
docker run -d --name demo-app -p 3000:3000 react-app
# -p host:container   Publish a container's port(s) to the host
```

### Execturing commands in running containers

Execute commands within a running container using the exec command.

```bash
docker exec c2 ls
docker exec -it c2 sh
```

### Stopping and starting containers

Create a new container using the docker run command, and restart a stopped container using docker start.

```bash
docker stop c2
docker start c2
```

### Removing containers

```bash
docker rm c2
# container is running: stop the container before removing or force remove
docker rm -f c2
```

### Volumes

```bash
docker volume create app-data # Create a volume
docker volume inspect app-data # Display detailed information on one or more volumes
docker volume ls # List volumes
docker volume prune # Remove unused local volumes
docker volume rm app-data # Remove one or more volumes
```

```bash
docker run -d -p 3002:3000 -v app-data:/app/data --name c4 react-app
```

### Copying files b/w host and containers

```bash
docker cp c1:/app/log.txt .
docker cp ./log.txt c1:/app/
```

## Sharing the source code with a container

Publishing changes

- For production: build a new image
- For development: we don't want to build a new image every time.

```bash
docker run -d -p 3000:3000 -v ${PWD}:/app react-app:0.1
```

### Remove images and containers

```bash
docker container ls -aq # all the containers
docker rm -f $(docker container ls -aq)

docker rmi $(docker images -q)
# -q, --quiet           Only show image IDs
# -a, --all             Show all images (default hides intermediate images)
```

## Running multi container applications

### Yaml

```json
{
  "name": "Product Name",
  "price": 29.99,
  "isPublished": true,
  "variants": [
    {
      "variantName": "Variant 1",
      "variantPrice": 29.99
    },
    {
      "variantName": "Variant 2",
      "variantPrice": 39.99
    }
  ],
  "additionalField": {
    "field1": "value1",
    "field2": "value2"
  }
}
```

```yml
---
name: product name
price: 29.99
isPublished: true
variants:
  - variantName: Variant 1
    variantPrice: 29.99
  - variantName: Variant 2
    variantPrice: 39.99
additionalField:
  field1: value1
  field2: value2
```

### docker-compose.yml

```yml
services:
  frontend:
    build: ./frontend
    ports:
      - 3000:3000
  backend:
    build: ./backend
    ports:
      - 3001:3000
    environment:
      DB_URL: mongodb://db/vidly
  database:
    image: mongo:4.0-xenial
    ports:
      - 27017:27017
    volumes:
      - vidly:/data/db

volumes:
  vidly:
```

### Building images

```bash
docker-compose build
docker-compose build --no-cache
```

### Starting & Stopping the application

```bash
docker-compose up
docker-compose up -d
docker-compose up —-build

docker-compose down
```

### Viewing logs

```bash
docker-compose logs
docker-compose logs -f
docker logs 383 -f
```

### Publishing changes

```yml
services:
  frontend:
    build: ./frontend
    ports:
      - 3000:3000
    volumes:
      - ./frontend:/app

  backend:
    build: ./backend
    ports:
      - 3001:3001
    environment:
      DB_URL: mongodb://db/vidly
    volumes:
      - ./backend:/app

  database:
    image: mongo:4.0-xenial
    ports:
      - 27017:27017
    volumes:
      - vidly:/data/db

volumes:
  vidly:
```

### validate and display the configuration

```bash
docker-compose -f file-name.yml config
```

### Use Compose Watch

```yml
services:
  app:
    container_name: NodeJs
    build: .
    command: npm run dev
    ports:
      - 3000:3000
    develop:
      watch:
        - action: sync
          path: ./
          target: /app
          ignore:
            - node_modules/
        - action: rebuild
          path: package.json
```

```bash
docker-compose up --build --watch
```
