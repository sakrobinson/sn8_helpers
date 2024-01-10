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

Remember to save this documentation as `README.md` in the same directory as your script. This will allow users to view the instructions easily on platforms like GitHub, where Markdown is rendered when viewing the directory.
