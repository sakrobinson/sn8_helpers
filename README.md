# sn8_helpers
Helper files for working with sn8 (time series prediction) on bittensor

---

# get_hf_models.py

This script is designed to interact with the Hugging Face Hub to list and optionally download all files from a specified model repository. It is useful for users who wish to obtain model files for offline use or for integration into other applications.

## Prerequisites

Before running the script, ensure that you have the following prerequisites installed:

- Python 3.x
- `huggingface_hub` library (can be installed via pip with `pip install huggingface_hub`)

Additionally, you will need internet access to reach the Hugging Face Hub and permission to write to the target directory on your system.

## Usage

To use the script, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the script using Python:

```bash
python huggingface_model_downloader.py
```

The script will perform the following actions:

1. Connect to the Hugging Face Hub and list all files available in the specified model repository (`Taoshi/model_v4` by default).
2. Print the list of files to the console.
3. Prompt you to confirm whether you want to download the files.
4. If you confirm with `yes`, it will download all files to the specified target directory (`/root/time-series-prediction-subnet/mining_models/` by default).
5. If you do not confirm with `yes`, it will cancel the download process.

## Interpreting the Script Output

When you run the script, you will see output similar to the following:

```
The following files are available for download:
file1.bin
file2.json
file3.txt
Do you want to download the above files? (yes/no):
```

After reviewing the listed files, respond with `yes` to proceed with the download or `no` to cancel. If you proceed, the script will output the progress of each file being downloaded:

```
Downloaded file1.bin to /root/time-series-prediction-subnet/mining_models/
Downloaded file2.json to /root/time-series-prediction-subnet/mining_models/
Downloaded file3.txt to /root/time-series-prediction-subnet/mining_models/
```

Once the download is complete, you can navigate to the target directory to verify that the files have been downloaded successfully.

## Customization

If you wish to download files from a different Hugging Face model repository or to a different target directory, modify the `model_repo` and `target_directory` variables in the script accordingly.

## Troubleshooting

- If you encounter permission issues, ensure that you have the necessary write permissions for the target directory or run the script with elevated privileges.
- If the script fails to connect to the Hugging Face Hub, check your internet connection and any firewall or proxy settings that may be blocking access.

---
Certainly! Below is a sample README text that explains the purpose and usage of the Bash script:

---

# Update Symbolic Links Script (update_links.sh)

## Overview

This script is designed to update symbolic links for `.h5` model files in the Hugging Face model repository. It corrects the paths of symbolic links that point to model files, ensuring they reference the correct absolute paths after being moved to a new location.

## Prerequisites for update_links.sh

Before running this script, ensure that you have:

- A Bash shell environment.
- The correct permissions to modify the files in the target directories.
- downloaded .h5 files or links (use get_hf_models.py)

## Usage of update_links.sh

To use this script, follow these steps:

1. Place the script in the root directory of your model files ("/root/time-series-prediction-subnet/mining_models"), or update the `base_dir` and `link_dir` variables in the script to match your directory structure.
2. Make the script executable by running the following command in your terminal:

    ```bash
    chmod +x update_links.sh
    ```

3. Execute the script by running:

    ```bash
    ./update_links.sh
    ```

The script will automatically navigate to the directory containing the symbolic links, update each link to point to the correct absolute path of the target `.h5` file, and provide output for each updated link.

## What update_links.sh Does

- The script sets the base directory where the model files are expected to be (`base_dir`) and the directory containing the symbolic links (`link_dir`).
- It navigates to the directory containing the symbolic links.
- For each `.h5` symbolic link in the directory, the script:
  - Reads the target of the symbolic link.
  - Constructs the absolute path to the target file, assuming the target is relative to the link's location.
  - Moves to the base directory.
  - Removes the old symbolic link.
  - Creates a new symbolic link with the absolute path.
  - Prints a message indicating the update.
  - Moves back to the links directory to continue the process for the next link.

## update_links.sh Notes

- The script assumes that the target paths provided by the symbolic links are relative to the location of the links themselves.
- If the structure of your directories differs from the one expected by the script, you will need to modify the `base_dir` and `link_dir` variables accordingly.
- It is recommended to back up your symbolic links and target files before running this script to prevent data loss in case of unexpected issues.

---
