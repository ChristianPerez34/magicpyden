from typing import Any, List

from aiohttp import ClientResponse, ClientSession

from magicpyden.schema import (
    TokenListingItem,
    TokenListings,
    TokenMetadata,
    TokenOfferReceivedItem,
    TokenOffersReceived,
    TokenActivityItem,
    TokenActivities,
)


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
        """
        Retrieves token metadata by mint address
        :param token_mint: Mint Address of token/NFT
        :return: Token metadata
        """
        data = await self._request(route=f"tokens/{token_mint}")
        return TokenMetadata(**data)

    async def get_token_listings(self, token_mint: str) -> List[TokenListingItem]:
        """
        Retrieves listings for specified token/NFT mint address
        :param token_mint: Mint address of token/NFT
        :return: List of token listings
        """
        data = await self._request(route=f"tokens/{token_mint}/listings")
        return TokenListings.parse_obj(data).__root__

    async def get_token_offers_received(
        self, token_mint: str, offset: int = 0, limit: int = 100
    ) -> List[TokenOfferReceivedItem]:
        """
        Retrieves received offers for specified token/NFT mint address
        :param token_mint: Mint address of token/NFT
        :param offset: The number of items to skip
        :param limit: The number of items to return. Max 500
        :return: List of token offers received
        """
        kwargs = {"offset": offset, "limit": limit}
        data = await self._request(
            route=f"tokens/{token_mint}/offers_received", **kwargs
        )
        return TokenOffersReceived.parse_obj(data).__root__

    async def get_token_activities(
        self, token_mint: str, offset: int = 0, limit: int = 100
    ) -> List[TokenActivityItem]:
        """
        Retrieves activities for specified token/NFT mint address
        :param token_mint: Mint address of token/NFT
        :param offset: The number of items to skip
        :param limit: The number of items to return. Max 500
        :return: List of activities for specified token/NFT
        """
        kwargs = {"offset": offset, "limit": limit}
        data = await self._request(route=f"tokens/{token_mint}/activities", **kwargs)
        return TokenActivities.parse_obj(data).__root__
