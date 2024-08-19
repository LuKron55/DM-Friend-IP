# Raspberry Pi IP Notifier with Discord DM and Pinning

This Python script runs on a Raspberry Pi (or any Linux server) and monitors changes to your external IP address. When a change is detected, the script sends a direct message (DM) to a specified Discord user from your account and pins the message in the chat.

## Features

- **IP Monitoring**: Periodically checks your external IP address.
- **Discord Notification**: Sends a DM to your friend with the new IP address.
- **Message Pinning**: Automatically pins the sent message in the DM chat for easy reference.

## Prerequisites

- **Python 3.x** installed on your Raspberry Pi or Linux server.
- `requests` library:
  ```bash
  pip install requests


# A Discord account and user token. Note: Using a Discord token directly in scripts violates Discord's Terms of Service and can result in your account being banned. Use at your own risk.



### Installation

    Clone the repository:

    git clone https://github.com/lukron55/DM-Friend-IP.git
    cd DM-Friend-IP


### Install dependencies:


    pip install requests
    
### Edit the script:
Open ip_notifier.py and replace YOUR_DISCORD_TOKEN with your actual Discord user token.


### Usage

Run the script:
You can run the script directly:

    python3 ip_notifier.py

### Running in the background:

To keep the script running even after closing the terminal, use nohup:


    nohup python3 ip_notifier.py &
    
Alternatively, use screen or tmux to manage the session.

### Test the script:

You can test the script by connecting to a VPN or by manually changing your IP address to see if the notification is sent.

### How It Works

The script checks the external IP address every 5 minutes by default.
If a new IP address is detected, it sends a DM with the new IP address to your friend on Discord and pins the message in the chat.
The script will continue to monitor the IP address and send notifications only when changes occur.

### Security and Risks

**Use at Your Own Risk: This script uses your Discord user token, which is against Discord's ToS for automation. There's a risk of your account being banned if detected.
Keep Your Token Safe: Never share your token or commit it to public repositories.**

# Disclaimer

This project is intended for educational purposes. Use responsibly and be aware of the risks associated with using your Discord user token in this manner.
