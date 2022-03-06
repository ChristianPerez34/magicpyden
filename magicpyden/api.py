from typing import Any, List

from aiohttp import ClientResponse, ClientSession

from magicpyden.schema import (
    CollectionActivities,
    CollectionActivityItem,
    CollectionItem,
    CollectionListingItem,
    CollectionListings,
    CollectionStats,
    Collections,
    EscrowBalance,
    LaunchPadCollections,
    LaunchpadCollectionItem,
    TokenListingItem,
    TokenListings,
    TokenMetadata,
    TokenOfferReceivedItem,
    TokenOffersReceived,
    TokenActivityItem,
    TokenActivities,
    Tokens,
    WalletActivityItem,
    WalletActivities,
    WalletOfferMadeItem,
    WalletOfferReceivedItem,
    WalletOffersMade,
    WalletOffersReceived,
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

    async def get_wallet_tokens(
        self,
        wallet_address: str,
        offset: int = 0,
        limit: int = 100,
        listed_only: bool = True,
    ) -> List[TokenMetadata]:
        """
        Retrieves tokens/NFTs owned by specified wallet address
        :param wallet_address: Solana wallet address
        :param offset: The number of items to skip
        :param limit: The number of items to return. Max 500
        :param listed_only: Determines if only listed tokens should be retrieved
        :return: List of tokens/NFTS owned by specified wallet address
        """
        kwargs = {
            "offset": offset,
            "limit": limit,
            "listedOnly": str(listed_only).lower(),
        }
        data = await self._request(route=f"wallets/{wallet_address}/tokens", **kwargs)
        return Tokens.parse_obj(data).__root__

    async def get_wallet_activities(
        self, wallet_address: str, offset: int = 0, limit: int = 0
    ) -> List[WalletActivityItem]:
        """
        Retrieves wallet activities
        :param wallet_address: Solana wallet address
        :param offset: The number of items to skip
        :param limit: The number of items to return. Max 500
        :return: List of wallet activities
        """
        kwargs = {
            "offset": offset,
            "limit": limit,
        }
        data = await self._request(
            route=f"wallets/{wallet_address}/activities", **kwargs
        )
        return WalletActivities.parse_obj(data).__root__

    async def get_wallet_offers_made(
        self, wallet_address: str, offset: int = 0, limit: int = 100
    ) -> List[WalletOfferMadeItem]:
        """
        Retrieves offers made by specified wallet
        :param wallet_address: Solana wallet address
        :param offset: The number of items to skip
        :param limit: The number of items to return. Max 500
        :return: List of offers made
        """
        kwargs = {
            "offset": offset,
            "limit": limit,
        }
        data = await self._request(
            route=f"wallets/{wallet_address}/offers_made", **kwargs
        )
        return WalletOffersMade.parse_obj(data).__root__

    async def get_wallet_offers_received(
        self, wallet_address: str, offset: int = 0, limit: int = 0
    ) -> List[WalletOfferReceivedItem]:
        """
        Retrieves offers received by a wallet
        :param wallet_address: Solana wallet address
        :param offset: The number of items to skip
        :param limit: The number of items to return. Max 500
        :return: List of offers received
        """
        kwargs = {
            "offset": offset,
            "limit": limit,
        }
        data = await self._request(
            route=f"wallets/{wallet_address}/offers_received", **kwargs
        )
        return WalletOffersReceived.parse_obj(data).__root__

    async def get_wallet_escrow_balance(self, wallet_address: str):
        """
        Retrieves escrow balance for wallet
        :param wallet_address: Solana wallet address
        :return: Wallet escrow balance
        """
        data = await self._request(route=f"wallets/{wallet_address}/escrow_balance")
        return EscrowBalance(**data)

    async def get_collections(
        self, offset: int = 0, limit: int = 200
    ) -> List[CollectionItem]:
        """
        Retrieves collections
        :param offset: The number of items to skip
        :param limit: The number of items to return. Max 500
        :return: Available collections on Magic Eden
        """
        kwargs = {
            "offset": offset,
            "limit": limit,
        }
        data = await self._request(route="collections", **kwargs)
        return Collections.parse_obj(data).__root__

    async def get_collection_listings(
        self, collection_name: str, offset: int = 0, limit: int = 20
    ) -> CollectionListingItem:
        """
        Retrieves tokens/NFT listings for collection
        :param offset: The number of items to skip
        :param limit: The number of items to return. Max 20
        :return: List of listings for collection
        """
        kwargs = {
            "offset": offset,
            "limit": limit,
        }
        data = await self._request(
            route=f"collections/{collection_name}/listings", **kwargs
        )
        return CollectionListings.parse_obj(data).__root__

    async def get_collection_activities(
        self, collection_name: str, offset: int = 0, limit: int = 100
    ) -> List[CollectionActivityItem]:
        """
        Retrieves activities for collection
        :param offset: The number of items to skip
        :param limit: The number of items to return. Max 500
        :return: List of activities for collection
        """
        kwargs = {
            "offset": offset,
            "limit": limit,
        }
        data = await self._request(
            route=f"collections/{collection_name}/activities", **kwargs
        )
        return CollectionActivities.parse_obj(data).__root__

    async def get_collection_stats(self, collection_name: str):
        """
        Retrieves stats for collection
        :return: List of activities for collection
        """
        data = await self._request(
            route=f"collections/{collection_name}/stats",
        )
        return CollectionStats(**data)

    async def get_launchpad_collections(
        self, offset: int = 0, limit: int = 200
    ) -> List[LaunchpadCollectionItem]:
        kwargs = {
            "offset": offset,
            "limit": limit,
        }
        data = await self._request(route="launchpad/collections", **kwargs)
        return LaunchPadCollections.parse_obj(data).__root__
