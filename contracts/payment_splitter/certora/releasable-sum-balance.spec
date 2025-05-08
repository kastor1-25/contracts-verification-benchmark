import "helper/methods.spec";
import "helper/getters.spec";

rule releasable_sum_balance {
    assert getTotalReleasable() == getBalance();
}

