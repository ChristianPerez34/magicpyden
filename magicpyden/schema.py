from typing import List, Optional

from pydantic import BaseModel
from pydantic.utils import to_lower_camel

from magicpyden.types import Category


class CamelModel(BaseModel):
    class Config:
        alias_generator = to_lower_camel
        allow_population_by_field_name = True


class Attribute(BaseModel):
    trait_type: str
    value: str  # noqa: WPS110


class File(BaseModel):  # noqa: WPS110
    uri: Optional[str]
    type: Optional[str]


class Creator(BaseModel):
    address: str
    share: int


class Properties(BaseModel):
    files: List[File]
    category: Optional[str]
    creators: Optional[List[Creator]]


class TokenMetadata(CamelModel):
    name: str
    collection: Optional[str]
    mint_address: str
    owner: str
    supply: int
    update_authority: str
    primary_sale_happened: int
    seller_fee_basis_points: int
    animation_url: Optional[str]
    external_url: Optional[str]
    attributes: List[Attribute]
    properties: Properties
    delegate: Optional[str]


class Tokens(BaseModel):
    __root__: List[TokenMetadata]


class TokenListingItem(CamelModel):
    token_mint: str
    token_address: str
    seller: str
    price: int
    pda_address: str
    auction_house: str
    token_size: int


class TokenListings(BaseModel):
    __root__: List[TokenListingItem]


class TokenOfferReceivedItem(CamelModel):
    buyer: str
    price: float
    expiry: int
    token_mint: str
    pda_address: str
    auction_house: str
    token_size: int
    pda_address: str
    auction_house: str
    token_size: int


class TokenOffersReceived(BaseModel):
    __root__: List[TokenOfferReceivedItem]


class TokenActivityItem(CamelModel):
    token_mint: str
    buyer_referral: str
    signature: str
    type: str
    source: str
    collection_symbol: Optional[str]
    slot: int
    block_time: int
    seller: Optional[str]
    seller_referral: str
    price: float
    buyer: Optional[str]


class TokenActivities(BaseModel):
    __root__: List[TokenActivityItem]


class WalletActivityItem(CamelModel):
    collection: Optional[str]
    token_mint: str
    buyer_referral: str
    signature: str
    type: str
    source: str
    slot: int
    block_time: int
    buyer: Optional[str]
    seller: Optional[str]
    seller_referral: str
    price: float


class WalletActivities(BaseModel):
    __root__: List[WalletActivityItem]


class WalletOfferMadeItem(CamelModel):
    token_mint: str
    pda_address: str
    auction_house: str
    buyer_referral: str
    token_size: int
    buyer: str
    price: float
    expiry: int


class WalletOffersMade(BaseModel):
    __root__: List[WalletOfferMadeItem]


class WalletOfferReceivedItem(CamelModel):
    token_mint: str
    pda_address: str
    auction_house: str
    token_size: int
    buyer: str
    price: int
    expiry: int


class WalletOffersReceived(BaseModel):
    __root__: List[WalletOfferReceivedItem]


class EscrowBalance(CamelModel):
    buyer_escrow: Optional[str]
    balance: float


class CollectionItem(CamelModel):
    description: str
    symbol: str
    twitter: Optional[str]
    discord: Optional[str]
    website: Optional[str]
    categories: Optional[List[Category]]


class Collections(BaseModel):
    __root__: List[CollectionItem]


class CollectionListingItem(CamelModel):
    seller: Optional[str]
    pda_address: str
    auction_house: str
    token_size: int
    token_address: str


class CollectionListings(BaseModel):
    __root__: List[CollectionListingItem]


class CollectionActivityItem(CamelModel):  # noqa: WPS215
    seller: Optional[str]
    price: Optional[float]
    collection: str
    buyer_referral: str
    signature: str
    type: str
    source: str
    slot: int
    block_time: int
    buyer: Optional[Optional[str]]
    seller_referral: str


class CollectionActivities(BaseModel):
    __root__: List[CollectionActivityItem]


class CollectionStats(CamelModel):
    symbol: str
    avg_price_24hr: Optional[float]
    floor_price: Optional[float]
    listed_count: Optional[int]
    volume_all: Optional[float]


class LaunchpadCollectionItem(CamelModel):
    symbol: str
    price: Optional[float]
    name: str
    image: str
    description: str
    featured: Optional[bool]
    edition: Optional[str]
    size: int
    launch_datetime: Optional[str]


class LaunchPadCollections(BaseModel):
    __root__: List[LaunchpadCollectionItem]
