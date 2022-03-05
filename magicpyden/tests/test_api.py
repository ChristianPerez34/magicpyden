import asyncio
from asyncio import sleep

import pytest
from pytest_asyncio import fixture

from magicpyden.api import MagicEdenApi
from magicpyden.schema import TokenMetadata


@fixture
async def fixture_api():
    await asyncio.sleep(0)
    return MagicEdenApi()


@pytest.mark.asyncio
async def test_get_token_metadata(fixture_api: MagicEdenApi):
    token_mint = "ACcbkzxT3vyRqzKKbaFgwkY2hSaLGCF3BmCzDCew4vk8"
    token_metadata = await fixture_api.get_token_metadata(token_mint=token_mint)

    await sleep(0)
    assert isinstance(token_metadata, TokenMetadata)
    assert token_metadata.mint_address == token_mint


@pytest.mark.asyncio
async def test_get_token_listings(fixture_api: MagicEdenApi):
    token_mint = "ACcbkzxT3vyRqzKKbaFgwkY2hSaLGCF3BmCzDCew4vk8"
    token_listings = await fixture_api.get_token_listings(token_mint=token_mint)

    await sleep(0)
    assert isinstance(token_listings, list)


@pytest.mark.asyncio
async def test_get_token_offers_received(fixture_api: MagicEdenApi):
    token_mint = "ByDYrNUkGUQADpgUt28pEGVKFYStHH5X4ojWvtNpo3od"
    token_listings = await fixture_api.get_token_offers_received(token_mint=token_mint)

    await sleep(0)
    assert isinstance(token_listings, list)


@pytest.mark.asyncio
async def test_get_token_activities(fixture_api: MagicEdenApi):
    token_mint = "ByDYrNUkGUQADpgUt28pEGVKFYStHH5X4ojWvtNpo3od"
    token_listings = await fixture_api.get_token_activities(token_mint=token_mint)

    await sleep(0)
    assert isinstance(token_listings, list)
