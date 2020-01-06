from pathlib import Path

from indicoio.clients.base import IPARequestClient
from indicoio.errors import FileDoesNotExist
from indicoio.objects.document import Document


class Dataset(IPAObject):
    def __init__(self, *, id: int, **fields):
        super().__init__(id=id, **fields)


class DatasetBuilder(IPABuilder):
    def __init__(self, client: IPARequestClient, *, name: str, files: str = None):
        self.name = name
        self.files = files or []
        super().__init__(client)

    def add_files(self, *files: Document) -> Dataset:
        for _file in files:
            if not Path(_file).exists():
                raise FileDoesNotExist(_file)
            self.files.append(_file)
        return self

    def create(self) -> Dataset:
        file_metas = []
        for _file in self.files:
            with _file.open("rb") as f_upload:
                metadata_response = self.client.post(
                    "/storage/files/upload", files={"file0": (_file.name, f_upload)}
                )
                file_metas.extend(metadata_response)
        results = self.client.create_dataset(name=self.name)
        return Dataset(**results)
