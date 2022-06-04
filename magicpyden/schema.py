from typing import List, Optional

from pydantic import BaseModel, Field

from magicpyden.types import Category


class Attribute(BaseModel):
    trait_type: str
    value: str  # noqa: WPS110


class File(BaseModel):  # noqa: WPS110
    uri: str
    type: str


class Creator(BaseModel):
    address: str
    share: int


class Properties(BaseModel):
    files: List[File]
    category: Optional[str] = None
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


class MintAddress(BaseModel):
    token_mint: str = Field(..., alias="tokenMint")


class Listing(BaseModel):
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
    animation_url: Optional[str] = Field(default=None, alias="animationUrl")
    external_url: Optional[str] = Field(default=None, alias="externalUrl")
    attributes: List[Attribute]
    properties: Properties
    delegate: Optional[str] = None


class Tokens(BaseModel):
    __root__: List[TokenMetadata]


class ProgramDerivedAddress(BaseModel):
    pda_address: str = Field(..., alias="pdaAddress")
    auction_house: str = Field(..., alias="auctionHouse")
    token_size: int = Field(..., alias="tokenSize")


class TokenListingItem(MintAddress, ProgramDerivedAddress):
    token_address: str = Field(..., alias="tokenAddress")
    seller: str
    price: int


class TokenListings(BaseModel):
    __root__: List[TokenListingItem]


class BuyerRefferal(BaseModel):
    buyer_referral: str = Field(..., alias="buyerReferral")


class TokenOfferReceivedItem(MintAddress, ProgramDerivedAddress):
    buyer: str
    price: float
    expiry: int


class TokenOffersReceived(BaseModel):
    __root__: List[TokenOfferReceivedItem]


class TokenActivityItem(MintAddress, BuyerRefferal):
    signature: str
    type: str
    source: str
    collection_symbol: str = Field(..., alias="collectionSymbol")
    slot: int
    block_time: int = Field(..., alias="blockTime")
    seller: Optional[str] = None
    seller_referral: str = Field(..., alias="sellerReferral")
    price: float
    buyer: Optional[str] = None


class TokenActivities(BaseModel):
    __root__: List[TokenActivityItem]


class WalletActivityItem(Collection, MintAddress, BuyerRefferal):
    signature: str
    type: str
    source: str
    slot: int
    block_time: int = Field(..., alias="blockTime")
    buyer: Optional[str]
    seller: Optional[str]
    seller_referral: str = Field(..., alias="sellerReferral")
    price: float


class WalletActivities(BaseModel):
    __root__: List[WalletActivityItem]


class WalletOfferMadeItem(MintAddress, ProgramDerivedAddress, BuyerRefferal):
    buyer: str
    price: float
    expiry: int


class WalletOffersMade(BaseModel):
    __root__: List[WalletOfferMadeItem]


class WalletOfferReceivedItem(MintAddress, ProgramDerivedAddress):
    buyer: str
    price: int
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
    categories: Optional[List[Category]] = None


class Collections(BaseModel):
    __root__: List[CollectionItem]


class CollectionListingItem(Listing, ProgramDerivedAddress):
    token_address: str = Field(..., alias="tokenAddress")


class CollectionListings(BaseModel):
    __root__: List[CollectionListingItem]


class CollectionActivityItem(  # noqa: WPS215
    Listing, Market, Collection, BuyerRefferal
):
    signature: str
    type: str
    source: str
    slot: int
    block_time: int = Field(..., alias="blockTime")
    buyer: Optional[Optional[str]] = None
    seller_referral: str = Field(..., alias="sellerReferral")


class CollectionActivities(BaseModel):
    __root__: List[CollectionActivityItem]


class CollectionStats(Symbol):
    avg_price_24hr: int = Field(..., alias="avgPrice24hr")
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
