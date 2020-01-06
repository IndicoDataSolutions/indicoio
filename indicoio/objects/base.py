from indicoio.clients.base import IPARequestClient


class IPAObject(object):
    def __init__(self, **fields):
        for field_name, field_value in fields.items():
            setattr(field_name, field_value)


class IPABuilder(object):
    def __init__(self, client: IPARequestClient):
        self.client = client

    def create(self):
        raise NotImplementedError()
