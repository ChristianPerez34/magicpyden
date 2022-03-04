from pydantic import BaseModel, Field
from typing import List


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
