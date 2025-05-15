import "helper/methods.spec";

rule releasable_sum_balance {
    assert getTotalReleasable() == getBalance();
}

