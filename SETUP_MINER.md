# TAO Mining Setup Guide for Bittensor

This README provides a step-by-step guide to setting up a virtual machine for mining TAO on the Bittensor network.

## Prerequisites

Before you begin, ensure you have a VM with Ubuntu installed.

## Installation Steps

### Install PM2

Navigate to the home directory.

```bash
cd
```

Install npm, a package manager for Node.js.

```bash
sudo apt install npm
```

Install PM2 globally using npm.

```bash
sudo npm install pm2 -g
```

### Install Bittensor

Run the Bittensor installation script.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/opentensor/bittensor/master/scripts/install.sh)"
```

### Add Local Subtensor

Download the Docker installation script.

```bash
curl -fsSL https://get.docker.com -o install-docker.sh
```

Execute the Docker installation script.

```bash
sudo sh install-docker.sh
```

Download the specified version of Docker Compose.

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

Make the Docker Compose binary executable.

```bash
sudo chmod +x /usr/local/bin/docker-compose
```

Verify the Docker Compose installation.

```bash
docker-compose --version
```

Clone the Subtensor repository.

```bash
git clone https://github.com/opentensor/subtensor.git
```

Navigate to the Subtensor directory.

```bash
cd subtensor
```

Start the Subtensor local network.

```bash
docker-compose up -d
```

### Check Subtensor

Check the status of the local Subtensor network.

```bash
btcli s metagraph --subtensor.network local
```

### Regenerate Coldkey and Create Hotkey

Regenerate the coldkey for your wallet.

```bash
btcli wallet regen_coldkey
```

Create a new hotkey for your wallet.

```bash
btcli wallet new_hotkey
```

### Clone Subnet Repository and Set Up Specifications

Clone the repository for the specific subnet you want to join.

```bash
git clone https://github.com/taoshidev/time-series-prediction-subnet.git
```

Navigate to the cloned directory.

```bash
cd time-series-prediction-subnet
```

Create and activate a Python virtual environment.

```bash
python3 -m venv venv
```
```bash
. venv/bin/activate
```

Install the required Python packages.

```bash
pip install -r requirements.txt
```

Install the package in editable mode.

```bash
python -m pip install -e .
```

Set the PYTHONPATH environment variable.

```bash
export PYTHONPATH=/root/time-series-prediction-subnet
```

### Unstake TAO

Unstake TAO from the network - here we assume you are using Bittensor Guru like a gentleman. Otherwise replace the ss58key

```bash
btcli r undelegate --delegate_ss58key 5HK5tp6t2S59DywmHRWPBVJeJ86T61KjurYqeooqj8sREpeN --amount <X> --subtensor.network local
```

### Register Hotkey

Register your hotkey on the network (this will cost TAO).

```bash
btcli subnet register --netuid <YOUR_PREFERRED_NETUID> --wallet.name <YOUR_COLDKEY> --wallet.hotkey <YOUR_HOTKEY>
```

### Optional: Use Registration Sniper

Clone the registration sniper tool by evlar. (requires pexpect)

```bash
pip install pexpect
```

```bash
git clone https://github.com/evlar/registration_sniper.git
```

Or clone the registration sniper tool branch from sakrobinson (inferior in every way).

```bash
git clone https://github.com/sakrobinson/registration_sniper.git
```

### Disable Firewall and Update System

Disable the system firewall.

```bash
sudo ufw disable
```

Update the system packages.

```bash
sudo apt update
```

Pull the latest changes from the git repository.

```bash
git pull
```
