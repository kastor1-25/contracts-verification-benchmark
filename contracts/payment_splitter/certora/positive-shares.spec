import "helper/methods.spec";

rule positive_shares {
    uint index;
    address payee = getPayee(index);
    assert getShares(payee) > 0;
}

