from agents.contemplation import generate_contemplation
from integrations.discord import send_message


def run_daily_contemplation():
    topic, content = generate_contemplation()

    message = f"""
🕉️ DAILY CONTEMPLATION

📌 Topic: {topic}

🧠 Thought:
{content}
    """

    send_message(message)

    print("Sent contemplation to Discord")

