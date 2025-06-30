import "helper/methods.spec";
import "helper/invariants.spec";

// for all a, released[a] <= (totalReceived * shares[a] ) // totalShares

rule fair_split{

    requireInvariant shares_sum_eq_totalShares();
    requireInvariant released_sum_totalReleased();
    requireInvariant payee_shares_gt_zero();


    env e;
    uint index;

    //address addr = getPayee(index); //same thing as the following two lines, but with a getter

    require index < currentContract.payees.length;
    address addr = currentContract.payees[index];

    uint addrReleased = getReleased(addr);
    uint addrShares = getShares(addr);

    mathint totalReceived = getBalance() + currentContract.totalReleased;

    // Choose one
    
    // assert addrReleased + releasable(addr) == totalReceived * currentContract.shares[addr] / currentContract.totalShares;
    assert addrReleased <= totalReceived * currentContract.shares[addr] / currentContract.totalShares;
}