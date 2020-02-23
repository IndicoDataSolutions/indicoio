from indicoio.client.client import RequestProxy
from typing import List


class StorageClient(RequestProxy):
    def upload_files(self, paths: List[str]):
        files = {
            path: open(path, "rb")
            for path in paths
        }
        return self.post("/api/storage/files/upload?upload_type=user", files=files)
