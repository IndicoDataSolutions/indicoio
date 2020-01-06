from .base import IPARequestClient


class Indico(IPARequestClient):
    def get_client(self, client_cls):
        return client_cls(config_options=self.config_options)
