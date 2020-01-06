from .base import IPARequestClient


class DatasetClient(IPARequestClient):
    def new(self, *, name: str):
        return DatasetBuilder(name)
