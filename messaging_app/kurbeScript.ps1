# Check if Minikube is installed
if (-not (Get-Command minikube -ErrorAction SilentlyContinue)) {
    Write-Host "Minikube is not installed. Please install it first."
    exit 1
}

# Start Minikube
Write-Host "Starting Minikube..."
minikube start --driver=docker

# Verify the cluster is running
Write-Host "Verifying cluster..."
kubectl cluster-info

# List available pods
Write-Host "Listing pods..."
kubectl get pods
