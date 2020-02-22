from indicoio.client.client import RequestProxy
from typing import List


class StorageClient(RequestProxy):
    def upload_files(self, large_document_paths: List[str]):
        files = {
            f"file_{idx}": open(file, "rb")
            for idx, file in enumerate(large_document_paths)
        }
        return self.post("/api/storage/files/upload?upload_type=user", files=files)
