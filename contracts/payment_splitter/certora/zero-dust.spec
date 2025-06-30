import "helper/methods.spec";
import "helper/invariants.spec";

/* rule zero_dust {

    requireInvariant shares_sum_eq_totalShares();
    requireInvariant released_sum_totalReleased();

    uint index1;
    uint index2;
    uint index3;

    require index1 < 3;
    require index2 < 3;
    require index3 < 3;

    require index1 != index2 && index1 != index3 && index2 != index3;
    require currentContract.payees[index1] != currentContract.payees[index2];
    require currentContract.payees[index1] != currentContract.payees[index3];
    require currentContract.payees[index2] != currentContract.payees[index3];

    assert currentContract.getTotalReleasable() == getBalance();
} */

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


/* invariant unique_payees (uint i, uint j)
    i != j &&
    currentContract.shares[currentContract.payees[i]] > 0 &&
    currentContract.shares[currentContract.payees[j]] > 0 =>
    i < currentContract.payees.length &&
    j < currentContract.payees.length &&
    currentContract.payees[i] != currentContract.payees[j]; 
 */
/* 
invariant unique_payees ()
    forall uint i. forall uint j. (i != j &&
    currentContract.shares[currentContract.payees[i]] > 0 &&
    currentContract.shares[currentContract.payees[j]] > 0 =>
    i < currentContract.payees.length &&
    j < currentContract.payees.length &&
    currentContract.payees[i] != currentContract.payees[j]); */



invariant unique_payees ()
    forall uint i. forall uint j.
    i != j =>
    currentContract.payees[i] != currentContract.payees[j];

