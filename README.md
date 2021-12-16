# What is host's IP

## Description

This project contains 2 containers (Pods):
* [A flask application](src) which returns its host external IP
* [An Nginx application](nginx) which used as a reversed proxy for all incoming requests

Those applications can work on [Docker Compose](https://docs.docker.com/compose/), or on [Minikube](https://minikube.sigs.k8s.io/) / [Kubernetes](https://kubernetes.io/) (using [Helm](https://helm.sh/)) 
(Created by mr-anderson86, started @12/2021)

## Prerequisites
### For Docker Compose
* Docker
### For Kubernetes
* minikube (or a kubernetes cluster)
* helm

## Usage

### To start the applications
* Via Docker Compose:  
  (need Docker installed on your host/computer)
```bash
git clone https://github.com/mr-anderson86/what_is_host_ip.git
cd what_is_host_ip
docker-compose up -d
```

* Via Minikube/Kubernetes (using Helm):
```bash
git clone https://github.com/mr-anderson86/minimarket_kubernetes.git
cd what_is_host_ip/kubernetes/helm
# helm install [your app name] host-ip, example below:
helm install host-ip host-ip

# Only for minikube:
minikube tunnel

# Note: in minikube also the 2 below commands can work instead of "minikube tunnel":
# minikube service nginx-service --url -n my-host-ip  # but this will give you a different port than 80
# kubectl -n my-host-ip port-forward --address 0.0.0.0 service/nginx-service 80:80

# If you are using an external k8s cluster, then you'll have to retrieve ip from external LB
```

That's it!  
Then all you need is to do is open your browser and go to http://localhost/  
And there you will see the external IP address of the host.  
(You can also go to http://localhost/api to get full json data)

### To stop the applications
* Via Docker:  
  (from the same directory type this command)
```bash
docker-compose down
```

* Via Helm:
```bash
helm uninstall [your app name]
```