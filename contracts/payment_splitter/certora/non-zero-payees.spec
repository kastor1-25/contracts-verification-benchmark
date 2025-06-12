import "helper/methods.spec";
import "helper/invariants.spec";

rule non_zero_payees {
    uint index;
    address addr = getPayee(index);
    // require !lastReverted;
    
    assert addr != 0;
}

