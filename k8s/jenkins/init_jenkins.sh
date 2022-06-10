# run if k8s deployment is deleted or needs to be created
# also requires webhook relay and dockerhub secrets deployed to devops-tools namespace
kubectl create namespace devops-tools
kubectl apply -f jenkins-pvc.yaml -n devops-tools
kubectl apply -f jenkins-full-deployment.yaml -n devops-tools
kubectl create rolebinding service-access --clusterrole=edit --serviceaccount=devops-tools:default -n devops-tools
kubectl create rolebinding service-access1 --clusterrole=edit --serviceaccount=devops-tools:default
kubectl create rolebinding service-access2 --clusterrole=edit --serviceaccount=default:default
