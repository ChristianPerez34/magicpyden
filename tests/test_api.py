import asyncio
from asyncio import sleep

import pytest
from pytest_asyncio import fixture

from magicpyden import MagicEdenApi
from magicpyden.schema import CollectionStats, EscrowBalance, TokenMetadata


@pytest.fixture
def event_loop():
    yield asyncio.get_event_loop()


@fixture
async def fixture_api():
    await asyncio.sleep(0)
    yield MagicEdenApi()


async def test_get_token_metadata(fixture_api: MagicEdenApi):
    token_mint = "ACcbkzxT3vyRqzKKbaFgwkY2hSaLGCF3BmCzDCew4vk8"

    async with fixture_api as api:
        token_metadata = await api.get_token_metadata(token_mint=token_mint)

    assert isinstance(token_metadata, TokenMetadata)
    assert token_metadata.mint_address == token_mint
    await sleep(1)


async def test_get_token_listings(fixture_api: MagicEdenApi):
    token_mint = "ACcbkzxT3vyRqzKKbaFgwkY2hSaLGCF3BmCzDCew4vk8"

    async with fixture_api as api:
        token_listings = await api.get_token_listings(token_mint=token_mint)

    assert isinstance(token_listings, list)
    await sleep(1)


async def test_get_token_offers_received(fixture_api: MagicEdenApi):
    token_mint = "ByDYrNUkGUQADpgUt28pEGVKFYStHH5X4ojWvtNpo3od"

    async with fixture_api as api:
        token_offers_received = await api.get_token_offers_received(
            token_mint=token_mint
        )

    assert isinstance(token_offers_received, list)
    await sleep(1)


async def test_get_token_activities(fixture_api: MagicEdenApi):
    token_mint = "ByDYrNUkGUQADpgUt28pEGVKFYStHH5X4ojWvtNpo3od"

    async with fixture_api as api:
        token_activities = await api.get_token_activities(token_mint=token_mint)

    assert isinstance(token_activities, list)
    await sleep(1)


async def test_get_wallet_tokens(fixture_api: MagicEdenApi):
    wallet_address = "8C1iDS8cN2eihPTVTfPtudEsa7gkFUFFXjoL3csuYMA"

    async with fixture_api as api:
        owned_tokens = await api.get_wallet_tokens(wallet_address=wallet_address)

    assert isinstance(owned_tokens, list)
    await sleep(1)


async def test_get_wallet_activities(fixture_api: MagicEdenApi):
    wallet_address = "8C1iDS8cN2eihPTVTfPtudEsa7gkFUFFXjoL3csuYMA"

    async with fixture_api as api:
        wallet_activities = await api.get_wallet_activities(
            wallet_address=wallet_address
        )

    assert isinstance(wallet_activities, list)
    await sleep(1)


async def test_get_wallet_offers_made(fixture_api: MagicEdenApi):
    wallet_address = "8C1iDS8cN2eihPTVTfPtudEsa7gkFUFFXjoL3csuYMA"

    async with fixture_api as api:
        wallet_offers_made = await api.get_wallet_offers_made(
            wallet_address=wallet_address
        )

    assert isinstance(wallet_offers_made, list)
    await sleep(1)


async def test_get_wallet_offers_received(fixture_api: MagicEdenApi):
    wallet_address = "8C1iDS8cN2eihPTVTfPtudEsa7gkFUFFXjoL3csuYMA"

    async with fixture_api as api:
        wallet_offers_received = await api.get_wallet_offers_received(
            wallet_address=wallet_address
        )

    assert isinstance(wallet_offers_received, list)
    await sleep(1)


async def test_get_wallet_escrow_balance(fixture_api: MagicEdenApi):
    wallet_address = "8C1iDS8cN2eihPTVTfPtudEsa7gkFUFFXjoL3csuYMA"

    async with fixture_api as api:
        wallet_ecsrow = await api.get_wallet_escrow_balance(
            wallet_address=wallet_address
        )

    assert isinstance(wallet_ecsrow, EscrowBalance)
    await sleep(1)


async def test_get_collections(fixture_api: MagicEdenApi):
    async with fixture_api as api:
        collections = await api.get_collections()

    assert isinstance(collections, list)
    await sleep(1)


async def test_get_collection_listings(fixture_api: MagicEdenApi):
    async with fixture_api as api:
        collection_listings = await api.get_collection_listings(
            collection_name="degods"
        )

    assert isinstance(collection_listings, list)
    await sleep(1)


async def test_get_collection_activities(fixture_api: MagicEdenApi):
    async with fixture_api as api:
        collection_activities = await api.get_collection_activities(
            collection_name="degods"
        )

    assert isinstance(collection_activities, list)
    await sleep(1)


async def test_get_collection_stats(fixture_api: MagicEdenApi):
    async with fixture_api as api:
        collection_stats = await api.get_collection_stats(collection_name="degods")

    assert isinstance(collection_stats, CollectionStats)
    await sleep(1)


async def test_get_launchpad_collections(fixture_api: MagicEdenApi):
    async with fixture_api as api:
        launchpad_collections = await api.get_launchpad_collections()

    assert isinstance(launchpad_collections, list)
    await sleep(1)
