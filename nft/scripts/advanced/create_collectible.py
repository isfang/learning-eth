from brownie import AdvancedCollectible
from scripts.helpful import *


def main():
    account = get_account()
    advanced = AdvancedCollectible[-1]
    fund_with_link(advanced.address, amount=Web3.toWei(0.1, "ether"))
    creation_transaction = advanced.createCollectible({"from": account})
    creation_transaction.wait(1)
    print("Collectible created!")
