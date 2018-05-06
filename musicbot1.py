import requests
from time import sleep

url = "https://api.telegram.org/bot592691084:AAG0zFToiDLtE3rK1M1NkMfyZI75nfcMH2o/"

def get_updates_json(request):
	params = {'timeout': 100, 'offset': None}
	response = requests.get(request + 'getUpdates', data=params)
	return response.json()

def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)

def main():
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
            send_mess(get_chat_id(last_update(get_updates_json(url))), 'А ща ещё лучше работать должно')
            update_id += 1
        sleep(1)

if __name__ == '__main__':
    main()