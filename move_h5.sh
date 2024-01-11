#!/bin/bash

# Define the base directory for the model files and the directory containing the symbolic links
base_dir="/root/time-series-prediction-subnet/mining_models"
link_dir="${base_dir}/models--Taoshi--model_v4/snapshots/f5c59804d57ef17390178123a216c00d17bc37d0"

# Navigate to the directory containing the symbolic links
cd "$link_dir"

# Loop through each .h5 symbolic link in the directory
for link in *.h5; do
    # Read the target of the symbolic link
    target=$(readlink "$link")
    
    # Construct the absolute path to the target file
    # Assuming the target is relative to the link's location
    target_path="${link_dir}/${target}"
    
    # Move to the base directory
    cd "$base_dir"
    
    # Remove the old symbolic link
    rm "$link"
    
    # Create a new symbolic link with the absolute path
    ln -s "$target_path" "$link"
    
    # Print a message indicating the update
    echo "Updated symbolic link for $link"
    
    # Move back to the links directory to continue the loop
    cd "$link_dir"
done

# End 
