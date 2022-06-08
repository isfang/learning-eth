from scripts.helpful import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import network
import pytest
from scripts.simple.deploy_create import deploy_create


def test_can_create_simple_collectible():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    simple_collectible = deploy_create()
    assert simple_collectible.ownerOf(0) == get_account()
