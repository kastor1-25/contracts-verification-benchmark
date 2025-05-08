import "helper/methods.spec";
import "helper/getters.spec";

rule zero_shares_fail {
    address addr;
    
    require getPayee(0) == addr;
    
    assert getShares(addr) == 0;
}

