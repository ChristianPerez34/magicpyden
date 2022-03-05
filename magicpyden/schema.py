from pydantic import BaseModel, Field
from typing import List, Optional


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


class TokenMetadata(BaseModel):
    mint_address: str = Field(..., alias="mintAddress")
    owner: str
    supply: int
    collection: str
    name: str
    update_authority: str = Field(..., alias="updateAuthority")
    primary_sale_happened: int = Field(..., alias="primarySaleHappened")
    seller_fee_basis_points: int = Field(..., alias="sellerFeeBasisPoints")
    image: str
    animation_url: str = Field(..., alias="animationUrl")
    external_url: str = Field(..., alias="externalUrl")
    attributes: List[Attribute]
    properties: Properties


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
