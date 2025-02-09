from mnnai import ServerError, change
from mnnai import url
import aiohttp
import json


async def Image(data):
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

        async with aiohttp.ClientSession() as session:
            async with session.post(f"{url}/v1/images/generations", headers=headers, json=payload, timeout=timeout) as response:
                return change(await response.json())
    except Exception:
        raise ServerError("Unexpected error :(")


async def Text(data):
    try:
        headers = {
            "Authorization": data["key"]
        }
        payload = {
            "model": data["model"],
            "messages": data["messages"],
            "stream": False
        }

        if data["debug"]:
            print(f"Sending a request to {url}/v1/chat/completions")

        async with aiohttp.ClientSession() as session:
            async with session.post(f"{url}/v1/chat/completions", headers=headers, json=payload) as response:
                return change(json.loads(await response.text()))
    except Exception:
        raise ServerError("Unexpected error :(")


async def StreamText(data):
    try:
        headers = {
            "Authorization": data["key"]
        }
        payload = {
            "model": data["model"],
            "messages": data["messages"],
            "stream": True
        }

        if data["debug"]:
            print(f"Sending a request to {url}/v1/chat/completions")

        async with aiohttp.ClientSession() as session:
            async with session.post(f"{url}/v1/chat/completions", headers=headers, json=payload) as response:
                async for chunk in response.content.iter_chunks():
                    lines = chunk[0].decode("utf-8").split('\n\n')
                    for line in lines:
                        line = line.replace("data:", "").strip()
                        if line and line != '[DONE]':
                            line = json.loads(line)
                            if "delta" in line["choices"][0]:
                                yield change(line)

    except Exception:
        raise ServerError("Unexpected error :(")
