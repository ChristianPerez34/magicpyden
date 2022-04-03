from typing import Any, List

from aiohttp import ClientResponse, ClientSession
from inflection import camelize

from magicpyden.endpoint import EndPoint
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

BASE_URL = "https://api-mainnet.magiceden.dev/v2"


class MagicEdenApi:
    def __init__(self, base_url: str = BASE_URL) -> None:
        """
        Initialize API object.

        :param base_url: Base url of Magic Eden API
        """
        self._base_url = base_url
        self._session: ClientSession = ClientSession(raise_for_status=True)

    async def __aenter__(self):
        """
        Create session on async enter.

        :return: MagicEden Api instance
        """
        if self._session.closed:
            self._session = ClientSession(raise_for_status=True)
        return self

    async def __aexit__(self, *err) -> None:
        """
        Close session on async exit.

        :param err: Error args
        """
        if not self._session.closed:
            await self._session.close()

    async def get_token_metadata(self, token_mint: str) -> TokenMetadata:
        """
        Retrieve token metadata by mint address.

        :param token_mint: Mint Address of token/NFT
        :return: Token metadata
        """
        json_data = await self._request(
            route=EndPoint.token_metadata.value.format(token_mint)
        )
        return TokenMetadata(**json_data)

    async def get_token_listings(self, token_mint: str) -> List[TokenListingItem]:
        """
        Retrieve listings for specified token/NFT mint address.

        :param token_mint: Mint address of token/NFT
        :return: List of token listings
        """
        json_data = await self._request(
            route=EndPoint.token_listings.value.format(token_mint)
        )
        return TokenListings.parse_obj(json_data).__root__

    async def get_token_offers_received(
        self, token_mint: str, offset: int = 0, limit: int = 100
    ) -> List[TokenOfferReceivedItem]:
        """
        Retrieve received offers for specified token/NFT mint address.

        :param token_mint: Mint address of token/NFT
        :param offset: The number of items to skip
        :param limit: The number of items to return. Max 500
        :return: List of token offers received
        """
        json_data = await self._request(
            route=EndPoint.token_offers_received.value.format(token_mint),
            offset=offset,
            limit=limit,
        )
        return TokenOffersReceived.parse_obj(json_data).__root__

    async def get_token_activities(
        self, token_mint: str, offset: int = 0, limit: int = 100
    ) -> List[TokenActivityItem]:
        """
        Retrieve activities for specified token/NFT mint address.

        :param token_mint: Mint address of token/NFT
        :param offset: The number of items to skip
        :param limit: The number of items to return. Max 500
        :return: List of activities for specified token/NFT
        """
        json_data = await self._request(
            route=EndPoint.token_activities.value.format(token_mint),
            offset=offset,
            limit=limit,
        )
        return TokenActivities.parse_obj(json_data).__root__

    async def get_wallet_tokens(
        self,
        wallet_address: str,
        offset: int = 0,
        limit: int = 100,
        listed_only: bool = True,
    ) -> List[TokenMetadata]:
        """
        Retrieve tokens/NFTs owned by specified wallet address.

        :param wallet_address: Solana wallet address
        :param offset: The number of items to skip
        :param limit: The number of items to return. Max 500
        :param listed_only: Determines if only listed tokens should be retrieved
        :return: List of tokens/NFTS owned by specified wallet address
        """
        json_data = await self._request(
            route=EndPoint.wallet_tokens.value.format(wallet_address),
            offset=offset,
            limit=limit,
            listed_only=str(listed_only).lower(),
        )
        return Tokens.parse_obj(json_data).__root__

    async def get_wallet_activities(
        self, wallet_address: str, offset: int = 0, limit: int = 100
    ) -> List[WalletActivityItem]:
        """
        Retrieve wallet activities.

        :param wallet_address: Solana wallet address
        :param offset: The number of items to skip
        :param limit: The number of items to return. Max 500
        :return: List of wallet activities
        """
        json_data = await self._request(
            route=EndPoint.wallet_activities.value.format(wallet_address),
            offset=offset,
            limit=limit,
        )
        return WalletActivities.parse_obj(json_data).__root__

    async def get_wallet_offers_made(
        self, wallet_address: str, offset: int = 0, limit: int = 100
    ) -> List[WalletOfferMadeItem]:
        """
        Retrieve offers made by specified wallet.

        :param wallet_address: Solana wallet address
        :param offset: The number of items to skip
        :param limit: The number of items to return. Max 500
        :return: List of offers made
        """
        json_data = await self._request(
            route=EndPoint.wallet_offers_made.value.format(wallet_address),
            offset=offset,
            limit=limit,
        )
        return WalletOffersMade.parse_obj(json_data).__root__

    async def get_wallet_offers_received(
        self, wallet_address: str, offset: int = 0, limit: int = 100
    ) -> List[WalletOfferReceivedItem]:
        """
        Retrieve offers received by a wallet.

        :param wallet_address: Solana wallet address
        :param offset: The number of items to skip
        :param limit: The number of items to return. Max 500
        :return: List of offers received
        """
        json_data = await self._request(
            route=EndPoint.wallet_offers_received.value.format(wallet_address),
            offset=offset,
            limit=limit,
        )
        return WalletOffersReceived.parse_obj(json_data).__root__

    async def get_wallet_escrow_balance(self, wallet_address: str):
        """
        Retrieve escrow balance for wallet.

        :param wallet_address: Solana wallet address
        :return: Wallet escrow balance
        """
        json_data = await self._request(
            route=EndPoint.wallet_escrow_balance.value.format(wallet_address)
        )
        return EscrowBalance(**json_data)

    async def get_collections(
        self, offset: int = 0, limit: int = 200
    ) -> List[CollectionItem]:
        """
        Retrieve collections.

        :param offset: The number of items to skip
        :param limit: The number of items to return. Max 500
        :return: Available collections on Magic Eden
        """
        json_data = await self._request(
            route=str(EndPoint.collections),
            offset=offset,
            limit=limit,
        )
        return Collections.parse_obj(json_data).__root__

    async def get_collection_listings(
        self, collection_name: str, offset: int = 0, limit: int = 20
    ) -> List[CollectionListingItem]:
        """
        Retrieve tokens/NFT listings for collection.

        :param collection_name: Name of NFT collection
        :param offset: The number of items to skip
        :param limit: The number of items to return. Max 20
        :return: List of listings for collection
        """
        json_data = await self._request(
            route=EndPoint.collection_listings.value.format(collection_name),
            offset=offset,
            limit=limit,
        )
        return CollectionListings.parse_obj(json_data).__root__

    async def get_collection_activities(
        self, collection_name: str, offset: int = 0, limit: int = 100
    ) -> List[CollectionActivityItem]:
        """
        Retrieve activities for collection.

        :param collection_name: Name of NFT collection
        :param offset: The number of items to skip
        :param limit: The number of items to return. Max 500
        :return: List of activities for collection
        """
        json_data = await self._request(
            route=EndPoint.collection_activities.value.format(collection_name),
            offset=offset,
            limit=limit,
        )
        return CollectionActivities.parse_obj(json_data).__root__

    async def get_collection_stats(self, collection_name: str):
        """
        Retrieve stats for collection.

        :return: List of activities for collection
        """
        json_data = await self._request(
            route=EndPoint.collection_stats.value.format(collection_name),
        )
        return CollectionStats(**json_data)

    async def get_launchpad_collections(
        self, offset: int = 0, limit: int = 200
    ) -> List[LaunchpadCollectionItem]:
        """
        Retrieve launchpad collections.

        :param offset: The number of items to skip
        :param limit: The number of items to return. Max 500
        :return: List of launchpad collections
        """
        json_data = await self._request(
            route=str(EndPoint.launchpad_collections), offset=offset, limit=limit
        )
        return LaunchPadCollections.parse_obj(json_data).__root__

    async def _request(self, route: str, **kwargs) -> Any:
        """
        Request data from defined ME endpoint.

        :param route: ME endpoint to target
        :param kwargs: Optional keyword arguments
        :return: JSON data
        """
        response: ClientResponse

        kwargs = {
            camelize(key) if key not in ("offset", "limit") else key: value
            for key, value in kwargs.items()  # noqa: WPS110
        }

        async with self._session.get(
            url=f"{self._base_url}/{route}", params=kwargs
        ) as response:
            return await response.json()
