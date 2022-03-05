import asyncio
from asyncio import sleep
from gc import collect

import pytest
from pytest_asyncio import fixture

from magicpyden.api import MagicEdenApi
from magicpyden.schema import EscrowBalance, TokenMetadata


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
    token_offers_received = await fixture_api.get_token_offers_received(
        token_mint=token_mint
    )

    await sleep(0)
    assert isinstance(token_offers_received, list)


@pytest.mark.asyncio
async def test_get_token_activities(fixture_api: MagicEdenApi):
    token_mint = "ByDYrNUkGUQADpgUt28pEGVKFYStHH5X4ojWvtNpo3od"
    token_activities = await fixture_api.get_token_activities(token_mint=token_mint)

    await sleep(0)
    assert isinstance(token_activities, list)


@pytest.mark.asyncio
async def test_get_wallet_tokens(fixture_api: MagicEdenApi):
    wallet_address = "8C1iDS8cN2eihPTVTfPtudEsa7gkFUFFXjoL3csuYMA"
    owned_tokens = await fixture_api.get_wallet_tokens(wallet_address=wallet_address)

    await sleep(0)
    assert isinstance(owned_tokens, list)


@pytest.mark.asyncio
async def test_get_wallet_activities(fixture_api: MagicEdenApi):
    wallet_address = "8C1iDS8cN2eihPTVTfPtudEsa7gkFUFFXjoL3csuYMA"
    wallet_activities = await fixture_api.get_wallet_activities(
        wallet_address=wallet_address
    )

    await sleep(0)
    assert isinstance(wallet_activities, list)


@pytest.mark.asyncio
async def test_get_wallet_offers_made(fixture_api: MagicEdenApi):
    wallet_address = "8C1iDS8cN2eihPTVTfPtudEsa7gkFUFFXjoL3csuYMA"
    wallet_offers_made = await fixture_api.get_wallet_offers_made(
        wallet_address=wallet_address
    )

    await sleep(0)
    assert isinstance(wallet_offers_made, list)


@pytest.mark.asyncio
async def test_get_wallet_offers_received(fixture_api: MagicEdenApi):
    wallet_address = "8C1iDS8cN2eihPTVTfPtudEsa7gkFUFFXjoL3csuYMA"
    wallet_offers_received = await fixture_api.get_wallet_offers_received(
        wallet_address=wallet_address
    )

    await sleep(0)
    assert isinstance(wallet_offers_received, list)


@pytest.mark.asyncio
async def test_get_wallet_escrow_balance(fixture_api: MagicEdenApi):
    wallet_address = "8C1iDS8cN2eihPTVTfPtudEsa7gkFUFFXjoL3csuYMA"
    wallet_ecsrow = await fixture_api.get_wallet_escrow_balance(
        wallet_address=wallet_address
    )

    await sleep(0)
    assert isinstance(wallet_ecsrow, EscrowBalance)


@pytest.mark.asyncio
async def test_get_collections(fixture_api: MagicEdenApi):
    collections = await fixture_api.get_collections()

    await sleep(0)
    assert isinstance(collections, list)
