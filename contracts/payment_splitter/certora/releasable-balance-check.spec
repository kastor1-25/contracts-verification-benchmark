import "helper/methods.spec";
import "helper/invariants.spec";
import "fair-split.spec";


rule releasable_balance_check {
    
    requireInvariant shares_sum_eq_totalShares();
    requireInvariant released_sum_totalReleased();
    requireInvariant payee_shares_gt_zero();

    requireInvariant out_of_bounds_payee();

    require currentContract.payees.length == 3;

    uint index;

    require index < currentContract.getPayeesLength();
/*     requireInvariant fair_split(index);
 */

    address payee = currentContract.payees[index];

    
    mathint releasable = releasable(payee);
    mathint balance = getBalance();
    
    assert releasable(payee) <= getBalance();
}