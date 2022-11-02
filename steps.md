# K8s talk

```shell
docker build . -t k8s-talk:latest
docker run -it -p 8000:8000 k8s-talk:latest

docker tag 3f682908da4e mneira011/k8s-talk:latest
docker push mneira011/k8s-talk:latest
```

Dockerhub link: https://hub.docker.com/r/mneira011/k8s-talk

```shell
kubectl create namespace k8s-talk
kubens k8s-talk

k get pods

kubectl apply -f deployment.yaml
k get pods


kubectl apply -f service.yaml


# binds to a specific pod!! Not to a service
kubectl port-forward svc/awesome-dogs-service 1234:80

kubectl scale deployments/awesome-dogs-deployment --replicas=2


# Ingress
k apply -f ingress.yaml
```
