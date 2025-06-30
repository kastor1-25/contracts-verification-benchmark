import "helper/methods.spec";
import "helper/invariants.spec";


rule swappable_call_order {
    requireInvariant shares_sum_eq_totalShares();
    requireInvariant released_sum_totalReleased();

    env e;

    uint index1;
    uint index2;

    require index1 != index2; //without this, certora imagines stuff
    
    require index1 < currentContract.payees.length;
    require index2 < currentContract.payees.length;

    address addr1 = currentContract.payees[index1];
    address addr2 = currentContract.payees[index2];

    storage initial = lastStorage; // 8 wei; 2 share

    release(e, addr1); // -> PaymentSplitter.call{value: v1} 4 wei -> 7
    release(e, addr2); // -> PaymentSplitter.call{value: v2} 4+3 -> 5
    storage final1 = lastStorage;// 4+5

    release(e, addr2) at initial; // -> PaymentSplitter.call{value: v2} 4 wei -> 5
    release(e, addr1);           // -> PaymentSplitter.call{value: v1}  4+2 -> 7
    storage final2 = lastStorage; //3+7 

    assert final1 == final2;
}






