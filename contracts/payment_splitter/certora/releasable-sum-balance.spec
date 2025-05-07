import "helper/erc20.spec";

rule releasable_sum_balance {
    assert getTotalReleasable() == getBalance();
}

