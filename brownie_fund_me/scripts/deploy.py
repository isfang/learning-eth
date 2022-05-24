from brownie import (
    FundMe,
    MockV3Aggregator,
    accounts,
    network,
    config
)
from scripts.helpful import (
    get_account,
    LocalBlockChainEnv,
    deploy_mocks
)


def deploy_fund():
    account = get_account()
    print(account)
    if network.show_active() not in LocalBlockChainEnv:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund()
