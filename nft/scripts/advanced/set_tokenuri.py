from lib2to3.pgen2 import token
from brownie import network, AdvancedCollectible
from scripts.helpful import (
    OPENSEA_URL,
    get_account,
    get_breed
)

dog_metadata_dic = {
    "PUG": "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json",
    "SHIBA_INU": "https://ipfs.io/ipfs/QmdryoExpgEQQQgJPoruwGJyZmz6SqV4FRTX1i73CT3iXn?filename=1-SHIBA_INU.json",
    "ST_BERNARD": "https://ipfs.io/ipfs/QmbBnUjyHHN7Ytq9xDsYF9sucZdDJLRkWz7vnZfrjMXMxs?filename=2-ST_BERNARD.json",
}


def main():
    print(f"Working on {network.show_active()}")
    advance = AdvancedCollectible[-1]
    number_of_collectibles = advance.tokenCounter()
    print(
        f"You have {number_of_collectibles} tokenIds type is {type(number_of_collectibles)}")
    for token_id in range(number_of_collectibles):
        print(
            f" token_id is {token_id} breed is {advance.tokenIdToBreed(token_id)}")
        breed = get_breed(advance.tokenIdToBreed(token_id))
        if not advance.tokenURI(token_id).startswith("https://"):
            print(f"Setting tokenURI of {token_id}")
            set_tokenURI(token_id, advance, dog_metadata_dic[breed])


def set_tokenURI(token_id, nft_contract, tokenURI):
    account = get_account()
    tx = nft_contract.setTokenURI(token_id, tokenURI, {"from": account})
    tx.wait(1)
    print(
        f"Awesome! You can view your NFT at {OPENSEA_URL.format(nft_contract.address, token_id)}"
    )
    print("Please wait up to 20 minutes, and hit the refresh metadata button")
