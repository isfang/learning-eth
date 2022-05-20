import json
from web3 import Web3

from solcx import compile_standard, install_solc
import os
from dotenv import load_dotenv

load_dotenv()

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

print("Installing")
install_solc("0.6.0")

dict = {
    "language": "Solidity",
    "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
    "settings": {
        "outputSelection": {
            "*": {
                "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"],
            }
        }
    },
}

compiled_sol = compile_standard(dict, solc_version="0.6.0")
with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)


bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# get abi
abi = json.loads(
    compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["metadata"]
)["output"]["abi"]


# for ganache local
# w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
# chain_id = 1337
# 这个地址与key是ganache上的
# my_address = "0x74Bb2A88633893052162c94Cb074CC90Bc06bcEE"
# private_key = "04a533bfb5716ae2d025944ef62674f5fbb0c4d56bce6b0afb7ebac8c6dde5ba"


# for infura
w3 = Web3(Web3.HTTPProvider(
    os.getenv("RINKEBY_RPC_URL")))
chain_id = 4
# 这个地址是 metamask 的地址与key
my_address = "0x89425Bfac90214a7F8C1588434E15858C5493Fb1"
private_key = "96f8cef0e6961056919dd04678f54de3eeedd285bdd717ae744e0941efd49a49"


SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
nonce = w3.eth.getTransactionCount(my_address)


transaction = SimpleStorage.constructor().buildTransaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": nonce,
    }
)

signed_txn = w3.eth.account.sign_transaction(
    transaction, private_key=private_key)
print("Deploying Contract!")

tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
print("Waiting for transaction to finish")


tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(f"Done! Contract deployed to {tx_receipt.contractAddress}")


simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
print(f"Initial Stored Value {simple_storage.functions.retrieve().call()}")

greeting_transaction = simple_storage.functions.store(15).buildTransaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": nonce + 1,
    }
)
sign_greeting_txn = w3.eth.account.sign_transaction(
    greeting_transaction, private_key=private_key
)
tx_greeting_hash = w3.eth.send_raw_transaction(
    sign_greeting_txn.rawTransaction
)
print("Updating stored Value..")
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_greeting_hash)

print(f"Updated Stored Value {simple_storage.functions.retrieve().call()}")
