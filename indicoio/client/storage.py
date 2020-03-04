from indicoio.client.client import RequestProxy
from typing import List
from pathlib import Path
import uuid
import simplejson as json


class StorageClient(RequestProxy):
    def upload(self, data: List[str]):
        """
        Calls user upload endpoint and returns the FileInput formatted representations
        """
        files = {}
        for datum in data:
            path = Path(datum)
            if path.exists():
                files[path.stem] = path.open("rb")
            else:
                files[str(uuid.uuid4())] = datum

        uploaded_files = self.post("/api/storage/files/store", files=files)

        return _parse_uploaded_files(uploaded_files)

    def download(self, url: str):
        relative_url = "/".join(url.split("/")[5:])
        full_url = f"{self.base_url}/api/storage/" + relative_url
        response = self.request_session.get(full_url)
        return response


def _parse_uploaded_files(uploaded_files: List[dict]):
    return [
        {
            "filename": f["name"],
            "filemeta": json.dumps(
                {"path": f["path"], "name": f["name"], "uploadType": f["upload_type"]}
            ),
        }
        for f in uploaded_files
    ]
