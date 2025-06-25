from kubernetes import client, config
import pprint

# Load kube config (assumes you're authenticated to AKS via kubectl)
config.load_kube_config()

# Initialize API clients
core_api = client.CoreV1Api()
custom_api = client.CustomObjectsApi()

# Get all pods in all namespaces
pods = core_api.list_pod_for_all_namespaces()

# Fetch metrics
metrics = custom_api.list_cluster_custom_object(
    group="metrics.k8s.io",
    version="v1beta1",
    plural="pods"
)

print("=== POD METRICS ===")
for item in metrics['items']:
    pod_name = item['metadata']['name']
    namespace = item['metadata']['namespace']
    containers = item['containers']
    print(f"\nPod: {namespace}/{pod_name}")
    for container in containers:
        name = container['name']
        usage = container['usage']
        cpu = usage['cpu']
        memory = usage['memory']
        print(f"  Container: {name}, CPU: {cpu}, Memory: {memory}")

# Get node metrics
node_metrics = custom_api.list_cluster_custom_object(
    group="metrics.k8s.io",
    version="v1beta1",
    plural="nodes"
)

print("\n=== NODE METRICS ===")
for node in node_metrics['items']:
    node_name = node['metadata']['name']
    usage = node['usage']
    cpu = usage['cpu']
    memory = usage['memory']
    print(f"Node: {node_name}, CPU: {cpu}, Memory: {memory}")
