# Taoshi's (v4) HF models here: https://huggingface.co/Taoshi/model_v4
# requires pip install huggingface_hub

from huggingface_hub import HfApi, hf_hub_download

# Initialize HfApi instance
api = HfApi()

# Define the repository and the target directory
model_repo = "Taoshi/model_v4"
target_directory = "/root/time-series-prediction-subnet/mining_models/" # this is the target dir. replace this

# List all files in the repository
repo_files = api.list_repo_files(repo_id=model_repo)

# Download each file to the target directory
for filename in repo_files:
    # Construct the full path for the target file
    target_file_path = f"{target_directory}{filename}"
    
    # Download the file
    hf_hub_download(
        repo_id=model_repo,
        filename=filename,
        cache_dir=target_directory  # This will download the file to the target directory
    )
    print(f"Downloaded {filename} to {target_directory}")
