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
