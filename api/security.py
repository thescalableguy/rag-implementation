from fastapi import Request, HTTPException
from collections import defaultdict
import time
import requests

# Track requests per IP
request_log = defaultdict(list)

# Blocked IPs
blocked_ips = set()

API_KEY = ""

def verify_api_key(request: Request):
    key = request.headers.get("x-api-key")

    if key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

# Config
RATE_LIMIT = 20
TIME_WINDOW = 60  # seconds

# Discord webhook (replace this)
DISCORD_WEBHOOK = ""


# Alert function
def send_alert(message):
    try:
        requests.post(DISCORD_WEBHOOK, json={"content": message})
    except:
        pass


# MAIN MIDDLEWARE
async def security_middleware(request: Request, call_next):
    ip = request.client.host
    now = time.time()

    # Already blocked
    if ip in blocked_ips:
        raise HTTPException(status_code=403, detail="Blocked")

    # Clean old requests
    request_log[ip] = [
        t for t in request_log[ip] if now - t < TIME_WINDOW
    ]

    request_log[ip].append(now)

    # THIS IS WHERE YOUR CODE GOES
    if len(request_log[ip]) > RATE_LIMIT:
        blocked_ips.add(ip)

        print(f"BLOCKED IP: {ip}")

        # 🔔 Alert
        send_alert(f"Suspicious IP blocked: {ip}")

        raise HTTPException(status_code=429, detail="Too many requests")

    # ✅ Continue request
    response = await call_next(request)
    return response
