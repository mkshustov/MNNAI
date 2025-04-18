from types import SimpleNamespace
import requests
import json

url = "https://api.mnnai.ru"
version = "5.4.0"

class ServerError(Exception):
    def send_data(self, data):
        raise ServerError("")

class VersionNotFoundError(Exception):
    def send_data(self, data):
        raise VersionNotFoundError("")

def change(d):
    if isinstance(d, dict):
        return SimpleNamespace(**{k: change(v) for k, v in d.items()})
    elif isinstance(d, list):
        return [change(i) for i in d]
    else:
        return d

def GetModels():
    response = requests.get(f"{url}/models").json()
    return json.dumps(response, indent=4, ensure_ascii=False)

def get_pypi_version():
    try:
        response = requests.get(f"https://pypi.org/pypi/mnnai/json").json()
        if response["info"]["version"] > version:
            print(f"New mnnai version: {response['info']['version']} (current: {version}) | pip install -U mnnai")
    except requests.RequestException as e:
        raise VersionNotFoundError(f"Failed to get PyPI version: {e}")

from mnnai.Generator import MNN

get_pypi_version()
