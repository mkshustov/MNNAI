from mnnai import ServerError, GetModels
from datetime import datetime
from mnnai import AI


def valid(messages):
    if not isinstance(messages, list):
        return False

    for message in messages:
        if not isinstance(message, dict):
            return False

        if not all(key in message for key in ["role", "content"]):
            return False

        if not isinstance(message["role"], str) or message["role"] not in ["user", "assistant", "system"]:
            return False

        if not isinstance(message["content"], str):
            return False

    return True



class MNN:
    def __init__(self, key: str = '', id: str = '', max_retries: int = 0, timeout: float = 600):
        if not key:
            raise ValueError("The API key is not filled in. Please provide a valid API key.")
        if not id:
            raise ValueError("The 'id' parameter must be filled in.")

        self.key = key
        self.id = id
        self.max_retries = max_retries
        self.timeout = timeout

    def Image_create(self, prompt: '', model: ''):
        start_time = datetime.now()
        if not prompt:
            raise ValueError("The 'prompt' parameter must be filled in.")
        if not model:
            raise ValueError("The 'model' parameter must be filled in.")

        data = {
            'prompt': prompt,
            'model': model,
            'id': self.id,
            'key': self.key,
            'max_retries': self.max_retries,
            'timeout': self.timeout
        }
        attempts = 0
        while attempts < self.max_retries + 1:
            if attempts >= 1:
                print(f"Attempt {attempts+1}")
            image = AI.Image(data=data)
            if 'Error' in image:
                if image['Error'] != 'Sorry, none of the providers responded, please use a different model':
                    raise ServerError(image['Error'])
                attempts += 1
            else:
                end_time = datetime.now()
                time = end_time - start_time
                image['data'][0]['time']['total time'] = str(time)
                return image
        raise ServerError('Sorry, none of the providers responded, please use a different model')

    def chat_create(self, model: str = '', messages: list = [], stream: bool = True, temperature: float = 0.5):
        start_time = datetime.now()
        if not messages:
            raise ValueError("The 'prompt' parameter must be filled in.")
        if not valid(messages):
            raise ValueError("Incorrect messages")
        if not 0.1 < temperature < 1:
            raise ValueError("Incorrect temperature")
        if not model:
            raise ValueError("The 'model' parameter must be filled in.")
        if not stream:
            raise ValueError("This function only support stream=True, for stream=False use chat_create")

        data = {
            'messages': messages,
            'model': model,
            'temperature': temperature,
            'id': self.id,
            'key': self.key,
            'max_retries': self.max_retries,
            'timeout': self.timeout
        }

        attempts = 0
        while attempts < self.max_retries + 1:
            if attempts >= 1:
                print(f"Attempt {attempts + 1}")
            text = AI.Text(data)
            if 'Error' in text:
                if text['Error'] != 'Sorry, none of the providers responded, please use a different model':
                    raise ServerError(text['Error'])
                attempts += 1
            else:
                end_time = datetime.now()
                time = end_time - start_time
                text['data'][0]['time']['total time'] = str(time)
                return text

        import time
        time.sleep(0.5)
        raise ServerError('Sorry, none of the providers responded, please use a different model')

    def GetModels(self):
        return GetModels()
