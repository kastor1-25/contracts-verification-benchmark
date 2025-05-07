import "helper/erc20.spec";

rule positive_shares {
    uint index;
    address payee = getPayee(index);
    assert getShares(payee) > 0;
}

