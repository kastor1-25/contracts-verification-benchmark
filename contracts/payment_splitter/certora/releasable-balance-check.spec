import "helper/methods.spec";

rule releasable_balance_check {
    uint index;
    address payee = getPayee(index);
    mathint releasable = releasable(payee);
    mathint balance = getBalance();
    assert releasable(payee) <= getBalance();
}

