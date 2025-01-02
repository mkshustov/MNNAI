from mnnai import ServerError
from mnnai import url
import requests


def Image(data):
    try:
        timeout = data["timeout"]
        headers = {
            "Content-Type": "application/json",
            "Authorization": data["key"],
            "Platform": "pc",
            "Id": data["id"]
        }
        payload = {
            "prompt": data["prompt"],
            "model": data["model"]
        }

        response = requests.post(f"{url}/v1/images/generations", headers=headers, json=payload, timeout=timeout)
        return response.json()

    except:
        raise ServerError("Unexpected error :(")



def Text(data):
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": data["key"],
            "Platform": "pc",
            "Id": data["id"]
        }
        payload = {
            "model": data["model"],
            "messages": data["messages"],
            "temperature": data["temperature"],
            "stream": False
        }

        response = requests.post(f"{url}/v1/chat/completion", headers=headers, json=payload)
        return response.json()

    except:
        raise ServerError("Unexpected error :(")
