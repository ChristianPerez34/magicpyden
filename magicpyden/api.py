from email.mime import base
from aiohttp import ClientSession


class MagicEdenApi:
    _Base_URL = "https://api-mainnet.magiceden.dev/v2"

    def __init__(
        self, base_url: str = _Base_URL, session: ClientSession = None
    ) -> None:
        self._base_url = base_url
        self._session = session

    async def __aenter__(self):
        if self._session is None:
            self._session = ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._session is None:
            await self._session.close()
