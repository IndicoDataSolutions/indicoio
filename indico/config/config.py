# -*- coding: utf-8 -*-

import os
from pathlib import Path

from indico.errors import IndicoInvalidConfigSetting


class IndicoConfig:
    """
    Configuration for the IndicoClient.

    Args:
        host= (str, optional): Indico Platform hostname (ie indico.myco.com)
        api_token_path= (str, optional): Path to the Indico API token file indico_api_token.txt

    Returns:
        IndicoConfig object

    Raises:
        RuntimeError: If api_token_path does not exist.

    Notes:
        By default, the IndicoConfig constructor will set host and api_token_path from the 
        INDICO_HOST and INDICO_API_TOKEN_PATH environment variables. If these variable are
        not set then it will use ``app.indico.io`` as the host and will look for the
        indico_api_token.txt file in the user's home directory.
    """
    host: str 
    protocol: str
    serializer: str
    api_token_path: str
    api_token: str = None

    def __init__(self, **kwargs):
        self.host: str = os.getenv("INDICO_HOST", "app.indico.io")
        self.protocol: str = os.getenv("INDICO_PROTOCOL", "https")
        self.serializer: str = os.getenv("INDICO_SERIALIZER", "msgpack")
        self.api_token_path: str = os.getenv("INDICO_API_TOKEN_PATH", Path.home()) 
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise IndicoInvalidConfigSetting(key)

        if not self.api_token:
            self.api_token_path, self.api_token = self._resolve_api_token()

    def _resolve_api_token(self):
        path = self.api_token_path
        if path is None:
            path = "."
        if not isinstance(path, Path):
            path = Path(path)
        if not path.exists():
            path = Path.home()
        if not path.is_file():
            path = path / "indico_api_token.txt"

        if not path.exists():
            raise RuntimeError(
                "Expected indico_api_token.txt in current directory, home directory, "
                "or provided as indicoio.config.token_path"
            )

        with path.open("r") as f:
            return path, f.read().strip()

