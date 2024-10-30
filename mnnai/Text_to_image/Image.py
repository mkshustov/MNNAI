from mnnai import ServerError, url
import requests


def Image(data):
    # Extracting the required data from the input dictionary
    timeout = data['timeout']
    headers = {
        'Content-Type': 'application/json',
        'Authorization': data['key'],
        'Platform': 'pc',
        'Id': data['id']
    }
    payload = {
        'prompt': data['prompt'],
        'model': data['model']
    }

    # Executing a POST request
    response = requests.post(f"{url}/v1/images/generations", headers=headers, json=payload, timeout=timeout)

    return response.json()



