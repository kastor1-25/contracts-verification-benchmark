import "helper/methods.spec";
import "helper/invariants.spec";


rule releasable_sum_balance {

    requireInvariant shares_sum_eq_totalShares();
    requireInvariant released_sum_totalReleased();
    
    mathint releasable = getTotalReleasable(); // hard to do with ghosts
    mathint balance = getBalance();

    assert getTotalReleasable() == getBalance();
}





