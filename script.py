import requests
import time

DISCORD_TOKEN = "YOUR_DISCORD_TOKEN"
FRIEND_USER_ID = "YOUR FRIENDS USER ID"
DM_API_URL = f"https://discord.com/api/v9/users/@me/channels"

headers = {
    "Authorization": DISCORD_TOKEN,
    "Content-Type": "application/json"
}

def get_external_ip():
    response = requests.get("https://api.ipify.org?format=json")
    return response.json().get("ip")

def send_discord_message(channel_id, message):
    payload = {"content": message}
    response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=payload)
    if response.status_code == 200:
        return response.json().get("id")
    return None

def pin_discord_message(channel_id, message_id):
    response = requests.put(f"https://discord.com/api/v9/channels/{channel_id}/pins/{message_id}", headers=headers)
    return response.status_code == 204

def get_dm_channel_id(friend_user_id):
    payload = {"recipient_id": friend_user_id}
    response = requests.post(DM_API_URL, headers=headers, json=payload)
    return response.json().get("id")

def main():
    current_ip = get_external_ip()
    channel_id = get_dm_channel_id(FRIEND_USER_ID)

    while True:
        new_ip = get_external_ip()
        if new_ip != current_ip:
            message = f"Your IP address has changed to {new_ip}"
            message_id = send_discord_message(channel_id, message)
            if message_id:
                pin_discord_message(channel_id, message_id)
            else:
                print("Failed to send message.")
            current_ip = new_ip
        time.sleep(300)

if __name__ == "__main__":
    main()
