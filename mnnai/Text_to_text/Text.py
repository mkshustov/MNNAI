from mnnai import ServerError, url
import json
import requests
import aiohttp


async def AsyncText(data):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': data['key'],
        'Platform': 'pc',
        'Id': data['id']
    }
    payload = {
        'model': data['model'],
        'messages': data['messages'],
        'temperature': data['temperature'],
        'stream': True
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(f"{url}/v1/chat/complection", headers=headers, json=payload) as response:
            if response.status == 404:
                raise ServerError('The server did not respond')
            async for chunk in response.content.iter_chunks():
                if chunk[0]:
                    yield json.loads(chunk[0].decode('utf-8'))


def Text(data):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': data['key'],
        'Platform': 'pc',
        'Id': data['id']
    }
    payload = {
        'model': data['model'],
        'messages': data['messages'],
        'temperature': data['temperature'],
        'stream': False
    }

    response = requests.post(f"{url}/v1/chat/complection", headers=headers, json=payload)
    if response.status_code == 404:
        raise ServerError('The server did not respond')
    return response.json()
