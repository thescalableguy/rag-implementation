import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1485165218106445854/dH811UAdCk9-MeOGcGMO41eBL6BwKtXfuZ4WOa_cm2NpJcW5aLcCAeAuahSZ1EhSbrL_"

requests.post(WEBHOOK_URL, json={
    "content": "Test message from UPSC AI 🚀"
})
