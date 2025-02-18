from mnnai import ServerError, GetModels
from mnnai import SyncAI, AsyncAI
from datetime import datetime


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


def check_input(messages, model):
    if not messages:
        raise ValueError("The 'prompt' parameter must be filled in.")
    if not valid(messages):
        raise ValueError("Incorrect messages")
    if not model:
        raise ValueError("The 'model' parameter must be filled in.")

class MNN:
    def __init__(self, key: str = '', max_retries: int = 0, timeout: float = 600, debug: bool = False):
        self.key = key
        self.max_retries = max_retries
        self.timeout = timeout
        self.debug = debug
        self.chat = Chat(key, max_retries, timeout, debug)
        self.images = Images(key, max_retries, timeout, debug)

    def GetModels(self):
        return GetModels()


class Images:
    def __init__(self, key, max_retries, timeout, debug):
        self.key = key
        self.max_retries = max_retries
        self.timeout = timeout
        self.debug = debug

    def create(self, prompt: '', model: ''):
        start_time = datetime.now()
        if self.debug:
            print("Analyzing information entered by the user")

        if not prompt:
            raise ValueError("The 'prompt' parameter must be filled in.")
        if not model:
            raise ValueError("The 'model' parameter must be filled in.")

        data = {
            'prompt': prompt,
            'model': model,
            'key': self.key,
            'max_retries': self.max_retries,
            'timeout': self.timeout,
            'debug': self.debug
        }
        attempts = 0
        while attempts < self.max_retries + 1:
            if attempts >= 1:
                print(f"Attempt {attempts+1}")
            image = SyncAI.Image(data=data)

            if getattr(image, 'Error', None):
                if image.Error != 'Sorry, none of the providers responded, please use a different model':
                    raise ServerError(image.Error)
                attempts += 1
            else:
                end_time = datetime.now()
                time = end_time - start_time
                setattr(image.data[0].time, "total time", str(time))
                return image
        raise ServerError('Sorry, none of the providers responded, please use a different model')

    async def async_create(self, prompt: '', model: ''):
        start_time = datetime.now()
        if self.debug:
            print("Analyzing information entered by the user")

        if not prompt:
            raise ValueError("The 'prompt' parameter must be filled in.")
        if not model:
            raise ValueError("The 'model' parameter must be filled in.")

        data = {
            'prompt': prompt,
            'model': model,
            'key': self.key,
            'max_retries': self.max_retries,
            'timeout': self.timeout,
            'debug': self.debug
        }
        attempts = 0
        while attempts < self.max_retries + 1:
            if attempts >= 1:
                print(f"Attempt {attempts+1}")
            image = await AsyncAI.Image(data=data)

            if getattr(image, 'Error', None):
                if image.Error != 'Sorry, none of the providers responded, please use a different model':
                    raise ServerError(image.Error)
                attempts += 1
            else:
                end_time = datetime.now()
                time = end_time - start_time
                setattr(image.data[0].time, "total time", str(time))
                return image
        raise ServerError('Sorry, none of the providers responded, please use a different model')


class Chat:
    def __init__(self, key, max_retries, timeout, debug):
        self.key = key
        self.max_retries = max_retries
        self.timeout = timeout
        self.debug = debug

    def create(self, messages: list, model: str = '', stream: bool = False, web_search: bool = False):
        if self.debug:
            print("Analyzing information entered by the user")

        check_input(messages, model)

        data = {
            'messages': messages,
            'model': model,
            'key': self.key,
            'max_retries': self.max_retries,
            'timeout': self.timeout,
            'stream': stream,
            'debug': self.debug,
            'web_search': web_search
        }

        attempts = 0
        while attempts < self.max_retries + 1:
            if attempts >= 1:
                if self.debug:
                    print(f"Attempt {attempts + 1}")

            text = SyncAI.Text(data)

            if getattr(text, 'Error', None):
                if text.Error != 'Sorry, none of the providers responded, please use a different model':
                    raise ServerError(text.Error)
                attempts += 1
            else:
                return text

        raise ServerError('Sorry, none of the providers responded, please use a different model')

    async def async_create(self, messages: list, model: str = '', stream: bool = False, web_search: bool = False):
        if self.debug:
            print("Analyzing information entered by the user")

        check_input(messages, model)

        data = {
            'messages': messages,
            'model': model,
            'key': self.key,
            'max_retries': self.max_retries,
            'timeout': self.timeout,
            'stream': stream,
            'debug': self.debug,
            'web_search': web_search
        }

        attempts = 0
        while attempts < self.max_retries + 1:
            if attempts >= 1:
                if self.debug:
                    print(f"Attempt {attempts + 1}")
            if stream:
                async def async_generator():
                    async for token in AsyncAI.StreamText(data):
                        yield token

                return async_generator()

            else:
                text = await AsyncAI.Text(data)

                if getattr(text, 'Error', None):
                    if text.Error != 'Sorry, none of the providers responded, please use a different model':
                        raise ServerError(text.Error)
                    attempts += 1
                else:
                    return text

        raise ServerError('Sorry, none of the providers responded, please use a different model')
