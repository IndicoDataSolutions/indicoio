from indicoio.client.client import RequestProxy
from typing import List
from pathlib import Path
import uuid


class StorageClient(RequestProxy):
    def upload_files(self, data: List[str]):
        files = {}
        for datum in data:
            if Path(datum).exists():
                files[datum] = open(datum, "rb")
            else:
                files[str(uuid.uuid4())] = datum
        return self.post("/api/storage/files/upload?upload_type=user", files=files)
