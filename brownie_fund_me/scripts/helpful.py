
from brownie import accounts, network, config, MockV3Aggregator

ForkedLocalEnv = ["mainnet-fork", "mainnet-fork-dev"]
LocalBlockChainEnv = ["development", "ganache-local"]

Decimals = 8
StartingPrice = 200000000000


def get_account():
    print(f"account env is {network.show_active()}")
    if (
        network.show_active() in LocalBlockChainEnv or
        network.show_active() in ForkedLocalEnv
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(Decimals, StartingPrice, {
            "from": get_account()
        })
    print("Mocks Deployed!")


def main():
    deploy_mocks()
