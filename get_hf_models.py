from huggingface_hub import HfApi, hf_hub_download

# Initialize HfApi instance
api = HfApi()

# Define the repository and the target directory
model_repo = "Taoshi/model_v4"
target_directory = "/root/time-series-prediction-subnet/mining_models/"

# List all files in the repository
repo_files = api.list_repo_files(repo_id=model_repo)

# Print out the files
print("The following files are available for download:")
for filename in repo_files:
    print(filename)

# Prompt the user for confirmation
user_input = input("Do you want to download the above files? (yes/no): ").strip().lower()
if user_input == "yes":
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
else:
    print("Download canceled.")
