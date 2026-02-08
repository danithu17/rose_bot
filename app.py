from flask import Flask, request
import requests

app = Flask(__name__)

# FB එකෙන් ගත්ත Token එක මෙතනට
PAGE_ACCESS_TOKEN = "EAAU3ZCH3BPhoBQmbw13TyPtB5QgaNvjf9OE6gg5gsFxEK7cHUZAZBeZBBisDPVBXeOSZBN8j4DBdcPQmkIZCxj5YE1kvNO3cXfh4aeqJ4kMG4F5Ut5OK6giC95FZCNhPpVflQsm8eXZAq69aegNWGLLZAXjkZCbyyg70QVBZBUITZCSpCc4XwNUk8AiRQZAszjruto3JSun666QZDZD"
# FB Webhook එකේදී දෙන රහස් වචනය
VERIFY_TOKEN = "rose_bot_2026"

@app.route("/", methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        return "Invalid verify token"

    if request.method == 'POST':
        data = request.get_json()
        if data["object"] == "page":
            for entry in data["entry"]:
                for messaging_event in entry["messaging"]:
                    if messaging_event.get("message"):
                        sender_id = messaging_event["sender"]["id"]
                        message_text = messaging_event["message"].get("text")
                        
                        # මෙතන තමයි "Reply" එක හදන්නේ
                        send_message(sender_id, f"අඩෝ මරු මැසේජ් එක: '{message_text}'! මම වැඩ බං.")
        return "ok", 200

def send_message(recipient_id, message_text):
    url = f"https://graph.facebook.com/v16.0/me/messages?access_token={PAGE_ACCESS_TOKEN}"
    payload = {"recipient": {"id": recipient_id}, "message": {"text": message_text}}
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run()
