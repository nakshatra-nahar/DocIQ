import os
import pprint

import dotenv
import requests
from flask import Flask, request

dotenv.load_dotenv()
dociq_url = os.getenv("dociq_url")
chatwoot_url = os.getenv("chatwoot_url")
dociq_key = os.getenv("dociq_key")
chatwoot_token = os.getenv("chatwoot_token")
# account_id = os.getenv("account_id")
# assignee_id = os.getenv("assignee_id")
label_stop = "human-requested"


def send_to_bot(sender, message):
    data = {
        'sender': sender,
        'question': message,
        'api_key': dociq_key,
        'embeddings_key': dociq_key,
        'history': ''
    }
    headers = {"Content-Type": "application/json",
               "Accept": "application/json"}

    r = requests.post(f'{dociq_url}/api/answer',
                      json=data, headers=headers)
    return r.json()['answer']


def send_to_chatwoot(account, conversation, message):
    data = {
        'content': message
    }
    url = f"{chatwoot_url}/api/v1/accounts/{account}/conversations/{conversation}/messages"
    headers = {"Content-Type": "application/json",
               "Accept": "application/json",
               "api_access_token": f"{chatwoot_token}"}

    r = requests.post(url,
                      json=data, headers=headers)
    return r.json()


app = Flask(__name__)


@app.route('/dociq', methods=['POST'])
def dociq():
    data = request.get_json()
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(data)
    try:
        message_type = data['message_type']
    except KeyError:
        return "Not a message"
    message = data['content']
    conversation = data['conversation']['id']
    contact = data['sender']['id']
    account = data['account']['id']
    assignee = data['conversation']['meta']['assignee']['id']
    print(account)
    print(label_stop)
    print(data['conversation']['labels'])
    print(assignee)

    if label_stop in data['conversation']['labels']:
        return "Label stop"
    # elif str(account) != str(account_id):
    #     return "Not the right account"

    # elif str(assignee) != str(assignee_id):
    #     return "Not the right assignee"

    if (message_type == "incoming"):
        bot_response = send_to_bot(contact, message)
        create_message = send_to_chatwoot(
            account, conversation, bot_response)
    else:
        return "Not an incoming message"

    return create_message


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
