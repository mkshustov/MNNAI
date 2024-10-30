url = 'https://mnnai.ru'

class ServerError(Exception):
    def send_data(self, data):
        raise ServerError("")

from mnnai.Generator import MNN
