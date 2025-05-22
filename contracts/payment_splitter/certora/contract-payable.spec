import "helper/methods.spec";

rule contract_payable {
    env e;
    uint256 amount;
    address a;

    require amount > 0;
    require balanceOf(a) >= amount;

    uint256 balanceBefore = getBalance();
    send(a, address(e.this), amount);

    assert getBalance() == balanceBefore + amount;
}