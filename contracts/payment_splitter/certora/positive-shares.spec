import "helper/methods.spec";
import "helper/getters.spec";

rule positive_shares {
    uint index;
    address payee = getPayee(index);
    assert getShares(payee) > 0;
}

