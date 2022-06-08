
from genericpath import samefile
from brownie import accounts
from scripts.helpful import get_account


from scripts.helpful import get_account, OPENSEA_URL
from brownie import SimpleCollectible

sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"


def deploy_create():
    account = get_account()

    simple = SimpleCollectible.deploy({"from": account})
    tx = simple.createCollectible(sample_token_uri, {"from": account})
    tx.wait(1)

    print(
        f"Awesome, you can view your NFT at {OPENSEA_URL.format(simple.address, simple.tokenCounter() - 1)}"
    )
    print("Please wait up to 20 minutes, and hit the refresh metadata button. ")

    return simple


def main():
    deploy_create()
