## K8s Hackaton

This repo contains a simple Flask app and a mariaDB database. (and an nginx proxy, which we won't use)

The program takes a integer as input and factorizes it. It stores the result to the database.


Goal: To set up deployment for the flask app and the mariaDB database.


#Preconfig:
------

Make sure that your docker daemon is running.
Start up minikube with 
minikube start

We need the our docker images to be available in minikube.

minikube docker-env
export DOCKER_TLS_VERIFY="1"
export DOCKER_HOST="tcp://127.0.0.1:49590"
export DOCKER_CERT_PATH="/Users/henrik/.minikube/certs"
export MINIKUBE_ACTIVE_DOCKERD="minikube"

To point your shell to minikube's docker-daemon, run:
 eval $(minikube -p minikube docker-env)

Now run the suggested command to point your shell to minikube's docker-daemon
eval $(minikube -p minikube docker-env)

To build all necessary images run
docker compose build

You should now be ready 


## TASKS
------

Task 1:
Make a deployment for a pod running a mariadb:10-focal image. (pulled from the public docker repo)

Task 2:
Make a deployment for a pod running the flask app: k8stutorial-backend

Task 3:
Make a service for the mariaDB pod.
  This must listen to port 6000 to work

Task 4:
Make a service for the backend pod.
  This needs to be available outside the cluster. 
  Hint: specify loadBalancer and NodePort


