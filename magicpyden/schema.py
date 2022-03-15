from lib2to3.pytree import Base
from typing import List, Optional

from pydantic import BaseModel, Field


class Attribute(BaseModel):
    trait_type: str
    value: str


class File(BaseModel):
    uri: str
    type: str


class Creator(BaseModel):
    address: str
    share: int


class Properties(BaseModel):
    files: List[File]
    category: str
    creators: List[Creator]


class Title(BaseModel):
    name: str


class Image(BaseModel):
    image: str


class Project(Title, Image):
    description: str


class Market(BaseModel):
    price: float


class Symbol(BaseModel):
    symbol: str


class Listing(BaseModel):
    token_mint: str = Field(..., alias="tokenMint")
    seller: Optional[str] = None


class Collection(BaseModel):
    collection: str


class TokenMetadata(Collection, Title):
    mint_address: str = Field(..., alias="mintAddress")
    owner: str
    supply: int
    update_authority: str = Field(..., alias="updateAuthority")
    primary_sale_happened: int = Field(..., alias="primarySaleHappened")
    seller_fee_basis_points: int = Field(..., alias="sellerFeeBasisPoints")
    animation_url: str = Field(..., alias="animationUrl")
    external_url: str = Field(..., alias="externalUrl")
    attributes: List[Attribute]
    properties: Properties
    delegate: Optional[str] = None


class Tokens(BaseModel):
    __root__: List[TokenMetadata]


class TokenListingItem(BaseModel):
    pda_address: str = Field(..., alias="pdaAddress")
    auction_house: str = Field(..., alias="auctionHouse")
    token_address: str = Field(..., alias="tokenAddress")
    token_mint: str = Field(..., alias="tokenMint")
    seller: str
    token_size: int = Field(..., alias="tokenSize")
    price: int


class TokenListings(BaseModel):
    __root__: List[TokenListingItem]


class TokenOfferReceivedItem(BaseModel):
    pda_address: str = Field(..., alias="pdaAddress")
    token_mint: str = Field(..., alias="tokenMint")
    auction_house: str = Field(..., alias="auctionHouse")
    buyer: str
    buyer_referral: str = Field(..., alias="buyerReferral")
    token_size: int = Field(..., alias="tokenSize")
    price: float
    expiry: int


class TokenOffersReceived(BaseModel):
    __root__: List[TokenOfferReceivedItem]


class TokenActivityItem(BaseModel):
    signature: str
    type: str
    source: str
    token_mint: str = Field(..., alias="tokenMint")
    collection_symbol: str = Field(..., alias="collectionSymbol")
    slot: int
    block_time: int = Field(..., alias="blockTime")
    buyer_referral: str = Field(..., alias="buyerReferral")
    seller: Optional[str] = None
    seller_referral: str = Field(..., alias="sellerReferral")
    price: float
    buyer: Optional[str] = None


class TokenActivities(BaseModel):
    __root__: List[TokenActivityItem]


class WalletActivityItem(Collection):
    signature: str
    type: str
    source: str
    token_mint: str = Field(..., alias="tokenMint")
    slot: int
    block_time: int = Field(..., alias="blockTime")
    buyer: Optional[str]
    buyer_referral: str = Field(..., alias="buyerReferral")
    seller: Optional[str]
    seller_referral: str = Field(..., alias="sellerReferral")
    price: float


class WalletActivities(BaseModel):
    __root__: List[WalletActivityItem]


class WalletOfferMadeItem(BaseModel):
    pda_address: str = Field(..., alias="pdaAddress")
    token_mint: str = Field(..., alias="tokenMint")
    auction_house: str = Field(..., alias="auctionHouse")
    buyer: str
    price: float
    token_size: int = Field(..., alias="tokenSize")
    expiry: int
    buyer_referral: Optional[str] = Field(None, alias="buyerReferral")


class WalletOffersMade(BaseModel):
    __root__: List[WalletOfferMadeItem]


class WalletOfferReceivedItem(BaseModel):
    pda_address: str = Field(..., alias="pdaAddress")
    token_mint: str = Field(..., alias="tokenMint")
    auction_house: str = Field(..., alias="auctionHouse")
    buyer: str
    price: int
    token_size: int = Field(..., alias="tokenSize")
    expiry: int


class WalletOffersReceived(BaseModel):
    __root__: List[WalletOfferReceivedItem]


class EscrowBalance(BaseModel):
    buyer_escrow: Optional[str]
    balance: float


class CollectionItem(Project, Symbol):
    twitter: Optional[str] = None
    discord: Optional[str] = None
    website: Optional[str] = None
    categories: Optional[List[Optional[str]]] = None


class Collections(BaseModel):
    __root__: List[CollectionItem]


class CollectionListingItem(Listing):
    pda_address: str = Field(..., alias="pdaAddress")
    auction_house: str = Field(..., alias="auctionHouse")
    token_address: str = Field(..., alias="tokenAddress")
    token_size: int = Field(..., alias="tokenSize")


class CollectionListings(BaseModel):
    __root__: List[CollectionListingItem]


class CollectionActivityItem(Listing, Market, Collection):
    signature: str
    type: str
    source: str
    slot: int
    block_time: int = Field(..., alias="blockTime")
    buyer: Optional[Optional[str]] = None
    buyer_referral: str = Field(..., alias="buyerReferral")
    seller_referral: str = Field(..., alias="sellerReferral")


class CollectionActivities(BaseModel):
    __root__: List[CollectionActivityItem]


class CollectionStats(Symbol):
    floor_price: int = Field(..., alias="floorPrice")
    listed_count: int = Field(..., alias="listedCount")
    volume_all: int = Field(..., alias="volumeAll")


class LaunchpadCollectionItem(Project, Market, Symbol):
    featured: Optional[bool] = None
    edition: Optional[str] = None
    size: int
    launch_datetime: Optional[str] = Field(default=None, alias="launchDatetime")


class LaunchPadCollections(BaseModel):
    __root__: List[LaunchpadCollectionItem]
