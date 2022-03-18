from enum import Enum


class EndPoint(Enum):
    token_metadata = "tokens/{0}"
    token_listings = "tokens/{0}/listings"
    token_offers_received = "tokens/{0}/offers_received"
    token_activities = "tokens/{0}/activities"
    wallet_tokens = "wallets/{0}/tokens"
    wallet_activities = "wallets/{0}/activities"
    wallet_offers_made = "wallets/{0}/offers_made"
    wallet_offers_received = "wallets/{0}/offers_received"
    wallet_escrow_balance = "wallets/{0}/escrow_balance"
    collections = "collections"
    collection_listings = "collections/{0}/listings"
    collection_activities = "collections/{0}/activities"
    collection_stats = "collections/{0}/stats"
    launchpad_collections = "launchpad/collections"

    def __str__(self):
        """
        Convert enum object to string.

        :return: Value of enum object
        """
        return self.value
