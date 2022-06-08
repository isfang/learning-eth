from scripts.helpful import (
    get_account,
    get_contract,
    fund_with_link
)
from brownie import AdvancedCollectible, network, config


def deploy_create():
    account = get_account()
    print(f"account is {account}")

    advanced = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["fee"],
        {"from": account},
    )
    fund_with_link(advanced.address)
    creating_tx = advanced.createCollectible({"from": account})
    creating_tx.wait(1)
    print("New token has been created!")
    return advanced, creating_tx


def main():
    deploy_create()
