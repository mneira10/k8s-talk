# K8s talk

## 1. Push image to registry

```shell
docker build . -t k8s-talk:latest
# To test image locally
docker run -it -p 8000:8000 k8s-talk:latest

docker tag k8s-talk:latest mneira011/k8s-talk:latest
docker push mneira011/k8s-talk:latest
```

Dockerhub link: https://hub.docker.com/r/mneira011/k8s-talk

## 2. Create deployment

```shell
kubectl create namespace k8s-talk
kubens k8s-talk

kubectl apply -f deployment.yaml

# Scale deployment
kubectl scale deployments/awesome-dogs-deployment --replicas=2

# To access locally:
kubectl port-forward <pod-name> 1234:8000

# To access globally:
ngrok http 1234
```

## 3. Create service

```shell
kubectl apply -f service.yaml


# binds to a specific pod!! Not to a service
kubectl port-forward svc/awesome-dogs-service 1234:80

# Get shell k8s & curl for page, ids should change
kubectl exec --stdin --tty <pod-name> -- /bin/bash

# in pod, curl should get different ids!
curl http://awesome-dogs-service
```

## 4. Create Ingress

```shell
# Ingress
k apply -f ingress.yaml
```

Visit http://dogs.cluster-test.upcodes.co
