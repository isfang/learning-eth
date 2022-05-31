

from os import access

from brownie import accounts
from brownie import accounts, config, network

LocalBlockChainEnvironments = ["hardhat",
                               "development", "ganache", "mainnet-fork"]

OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"
BREED_MAPPING = {0: "PUG", 1: "SHIBA_INU", 2: "ST_BERNARD"}


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if network.show_active() in LocalBlockChainEnvironments:
        return accounts[0]
    if id:
        return accounts.load(id)
    return accounts.add(config["wallets"]["from_key"])
