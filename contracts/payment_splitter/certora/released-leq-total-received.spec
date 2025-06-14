import "helper/methods.spec";
import "helper/invariants.spec";

// for all a, released[a] <= (totalReceived * shares[a] ) // totalShares

rule released_leq_total_received{

    requireInvariant shares_sum_eq_totalShares();
    requireInvariant released_sum_totalReleased();

    env e;
    uint index;

    //address addr = getPayee(index); //same thing as the following two lines, but with a getter

    require index < currentContract.payees.length;
    address addr = currentContract.payees[index];

    uint addrReleased = getReleased(addr);
    uint addrShares = getShares(addr);

    mathint totalReceived = getBalance() + currentContract.totalReleased;

    assert( addrReleased <= totalReceived * addrShares / currentContract.totalShares); 
}