from email.mime import base
from json import JSONDecodeError
from asyncio import sleep
from typing import Any, List
from aiohttp import ClientResponse, ClientSession

from magicpyden.exceptions import HttpException
from magicpyden.schema import TokenListingItem, TokenListings, TokenMetadata


class MagicEdenApi:
    _Base_URL = "https://api-mainnet.magiceden.dev/v2"

    def __init__(
        self, base_url: str = _Base_URL, session: ClientSession = None
    ) -> None:
        self._base_url = base_url
        self._session = session or ClientSession(raise_for_status=True)

    async def _request(self, route: str, **kwargs) -> Any:
        response: ClientResponse

        async with self._session.get(
            url=f"{self._base_url}/{route}", params=kwargs
        ) as response:
            return await response.json()

    async def get_token_metadata(self, token_mint: str) -> TokenMetadata:
        data = await self._request(route=f"tokens/{token_mint}")
        return TokenMetadata(**data)

    async def get_token_listings(self, token_mint: str) -> List[TokenListingItem]:
        data = await self._request(route=f"tokens/{token_mint}/listings")
        print(data)
        return TokenListings.parse_obj(data).__root__
