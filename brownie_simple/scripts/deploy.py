from curses import noecho
from brownie import accounts, config, SimpleStorage, network
from eth_typing import Primitives


# brownie run scripts/deploy.py --network rinkeby
# 目前的env 跟 config 的配置是配置的 infrua io 的 project id 跟 rinkeby网络下的 钱包 private key
# 可以在 https://rinkeby.etherscan.io/address/0x89425Bfac90214a7F8C1588434E15858C5493Fb1 这个地方查看发生的交易
def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})

    # 这个是个view的方法 所以可以不用加上 {"from": account}
    stored_value = simple_storage.retrieve()
    print(stored_value)

    transcation = simple_storage.store(15, {"from": account})
    transcation.wait(1)
    update_stored_value = simple_storage.retrieve()
    print(update_stored_value)


def get_account():
    print(f"network env is {network.show_active()}")
    if network.show_active() == "development":
        return accounts[0]
    else:
        # You can optionally specify a private key to access a specific account:
        return accounts.add(config["wallets"]["from_key"])

# ganache的本地账号的几种方法


def brownie_accout_simple():

    # 获取本地的ganache账号
    account = accounts[0]
    print(account)

    # 将自己的密钥导入到gananche 并生成地址 使用的时候需要输入密码
    # account_dong_test = accounts.load("dong-test")  # 执行的时候 需要我们输入密码
    # print(account_dong_test)

    # 通过环境变量


def main():
    # brownie_accout_simple()
    deploy_simple_storage()
