import "helper/methods.spec";
import "helper/getters.spec";

rule releasable_balance_check {
    uint index;
    address payee = getPayee(index);
    assert releasable(payee) <= getBalance();
}

