import "helper/methods.spec";
import "helper/invariants.spec";

rule releasable_balance_check {
    requireInvariant shares_sum_eq_totalShares();
    requireInvariant released_sum_totalReleased();
    
    uint index;
    address payee = getPayee(index);
    mathint releasable = releasable(payee);
    mathint balance = getBalance();
    
    assert releasable(payee) <= getBalance();
}

