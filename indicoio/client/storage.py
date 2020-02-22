from indicoio.client.client import RequestProxy
from typing import List


class StorageClient(RequestProxy):
    def upload_files(self, large_document_paths: List[str]):
        files = {
            file: open(file, "rb")
            for file in enumerate(large_document_paths)
        }
        return self.post("/api/storage/files/upload?upload_type=user", files=files)
