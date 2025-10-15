# kurbeScript.ps1

Write-Host "Starting Minikube..."
minikube start --driver=docker

Write-Host "`nCluster info:"
kubectl cluster-info

Write-Host "`nListing all pods in all namespaces:"
kubectl get pods --all-namespaces

Write-Host "`nDone!"
