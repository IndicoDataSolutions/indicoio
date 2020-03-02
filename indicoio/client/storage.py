from indicoio.client.client import RequestProxy
from typing import List
from pathlib import Path
import uuid
import simplejson as json


class StorageClient(RequestProxy):
    def upload(self, data: List[str]):
        files = {}
        for datum in data:
            path = Path(datum)
            if path.exists():
                files[path.stem] = path.open("rb")
            else:
                files[str(uuid.uuid4())] = datum
            
        uploaded_files = self.post("/api/storage/files/store", files=files)

        return _parse_uploaded_files(uploaded_files)
