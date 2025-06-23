import "helper/methods.spec";
import "helper/invariants.spec";


rule swappable_call_order {
    requireInvariant shares_sum_eq_totalShares();
    requireInvariant released_sum_totalReleased();

    env e1;
    env e2;

    require e1 == e2;

    uint index1;
    uint index2;

    require index1 != index2; //without this, certora imagines stuff
    
    require index1 < currentContract.payees.length;
    require index2 < currentContract.payees.length;

    address addr1 = currentContract.payees[index1];
    address addr2 = currentContract.payees[index2];

    uint addr1Released = getReleased(addr1);
    uint addr2Released = getReleased(addr2);

    storage initial = lastStorage;

    release(e1, addr1);
    release(e1, addr2);
    storage final1 = lastStorage;

    release(e2, addr2) at initial;
    release(e2, addr1);
    storage final2 = lastStorage;

    assert final1 == final2;
}






