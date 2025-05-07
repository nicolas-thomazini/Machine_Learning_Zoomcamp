import kagglehub

# Download latest version
path = kagglehub.dataset_download("agrigorev/clothing-dataset-full")

print("Path to dataset files:", path)