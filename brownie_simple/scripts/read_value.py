from brownie import SimpleStorage, accounts, config


def read_contract():

    # 这个地方写 -1 是代表永远获取最近部署的合约
    simple_storage = SimpleStorage[-1]
    print(simple_storage.retrieve())


def main():
    read_contract()
