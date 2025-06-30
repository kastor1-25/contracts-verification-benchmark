import "helper/methods.spec";
import "helper/invariants.spec";


//maybe this becomes an invariant if its useful, else delete

rule non_zero_payees {
    uint index;
    address addr = getPayee(index);
    requireInvariant payee_shares_gt_zero();
    requireInvariant shares_sum_eq_totalShares();
    requireInvariant released_sum_totalReleased();

    // require !lastReverted;
    
    assert addr != 0;
}

