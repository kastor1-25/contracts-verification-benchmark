import "helper/methods.spec";
import "helper/invariants.spec";

function callFunctionWithParams(env e, method f, address from, address to) {
    uint256 amount;

    if (f.selector == sig:transfer(address, uint256).selector) {
        require e.msg.sender == from;
        transfer(e, to, amount);
    } else if (f.selector == sig:allowance(address, address).selector) {
        allowance(e, from, to);
    } else if (f.selector == sig:approve(address, uint256).selector) {
        approve(e, to, amount);
    } else if (f.selector == sig:transferFrom(address, address, uint256).selector) {
        transferFrom(e, from, to, amount);
    } else if (f.selector == sig:increaseAllowance(address, uint256).selector) {
        increaseAllowance(e, to, amount);
    } else if (f.selector == sig:decreaseAllowance(address, uint256).selector) {
        decreaseAllowance(e, to, amount);
    } else if (f.selector == sig:mint(address, uint256).selector) {
        mint(e, to, amount);
    } else if (f.selector == sig:burn(address, uint256).selector) {
        burn(e, from, amount);
    } else {
        calldataarg args;
        f(e, args);
    }
}



rule swappable_call_order {
    requireInvariant shares_sum_eq_totalShares();
    requireInvariant released_sum_totalReleased();

    env e;
    method f;
    method g;
    uint index;
    
    require index1 < currentContract.payees.length;

    address addr = currentContract.payees[index];
    uint addrReleased = getReleased(addr);

    storage initial = lastStorage;

    callFunctionWithParams(e, f, addr);
    callFunctionWithParams(e, g, addr);
    storage final1 = lastStorage;

    callFunctionWithParams(e, g, addr) at initial;
    callFunctionWithParams(e, f, addr);
    storage final2 = lastStorage;

    assert final1 == final2;
}






