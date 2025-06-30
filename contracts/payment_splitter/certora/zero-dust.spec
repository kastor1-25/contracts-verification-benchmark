import "helper/methods.spec";
import "helper/invariants.spec";


rule zero_dust {

    requireInvariant shares_sum_eq_totalShares();
    requireInvariant released_sum_totalReleased();
    requireInvariant payee_shares_gt_zero();

    uint index1;
    uint index2;

    require index1 != index2;
    require index1 < currentContract.payees.length;
    require index2 < currentContract.payees.length;

 

    require currentContract.shares[currentContract.payees[index1]] > 0;
    require currentContract.shares[currentContract.payees[index2]] > 0;
    

/*     require currentContract.payees[index1] != currentContract.payees[index2];
 */
    assert currentContract.getTotalReleasable() == getBalance();
}
