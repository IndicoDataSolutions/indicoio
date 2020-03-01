from indicoio.client.client import RequestProxy
from typing import List
from pathlib import Path
import uuid


class StorageClient(RequestProxy):
    def upload(self, data: List[str]):
        files = {}
        for datum in data:
            path = Path(datum)
            if path.exists():
                files[datum.stem] = path.open("rb")
            else:
                files[str(uuid.uuid4())] = datum
        return self.post("/api/storage/files/store", files=files)
