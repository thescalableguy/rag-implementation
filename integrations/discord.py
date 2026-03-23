import requests

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1485316851616583741/OrM50aA1M_hZzStn59B0XB-CKG9UZ5PxlVrkHZnVV7W2W4_VThI8Nl27PmALaYawLM9P"


def send_message(message: str):
    try:
        requests.post(DISCORD_WEBHOOK, json={"content": message})
    except Exception as e:
        print("Discord error:", e)
