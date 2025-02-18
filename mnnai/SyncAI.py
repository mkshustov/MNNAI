from mnnai import ServerError, change
from mnnai import url
import requests
import json

def Image(data):
    try:
        timeout = data["timeout"]
        headers = {
            "Content-Type": "application/json",
            "Authorization": data["key"]
        }
        payload = {
            "prompt": data["prompt"],
            "model": data["model"]
        }

        if data["debug"]:
            print(f"Sending a request to {url}/v1/images/generations")

        response = requests.post(f"{url}/v1/images/generations", headers=headers, json=payload, timeout=timeout)
        return change(response.json())

    except:
        raise ServerError("Unexpected error :(")


def Text(data):
    try:
        headers = {
            "Authorization": data["key"]
        }
        payload = {
            "model": data["model"],
            "messages": data["messages"],
            "stream": data["stream"],
            "web_search": data["web_search"]
        }

        if data["debug"]:
            print(f"Sending a request to {url}/v1/chat/completions")

        response = requests.post(f"{url}/v1/chat/completions", headers=headers, json=payload)

        res = []
        if data["stream"]:
            for token in response.text.split('\n'):
                if token:
                    token = token[5:]
                    if token != " [DONE]":
                        token = json.loads(token)
                        if "delta" in token["choices"][0]:
                            res.append(change(token))
            return res

        else:
            return change(response.json())
    except:
        raise ServerError("Unexpected error :(")
