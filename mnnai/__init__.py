url = 'http://127.0.0.1:8080'
class ServerError(Exception):
    def send_data(self, data):
        raise ServerError("")

from mnnai.Generator import MNN