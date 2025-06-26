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

    uint index1;
    uint index2;

    require currentContract.shares[currentContract.payees[index1]] > 0;
    require currentContract.shares[currentContract.payees[index2]] > 0;

    require index1 != index2;
    require currentContract.payees[index1] != currentContract.payees[index2];

    assert currentContract.getTotalReleasable() == getBalance();
} 


 /* example of preserved block
 
  invariant solvencyAsInv() asset.balanceOf() >= internalAccounting() {
  preserved withdrawExcess(address token)  {
      require token != asset; 
  }
} */


 
/* strong invariant zero_dust  ()
    currentContract.getTotalReleasable() == getBalance() {
        preserved {
            requireInvariant shares_sum_eq_totalShares();
            requireInvariant released_sum_totalReleased();
        }
    } */