import "helper/methods.spec";
import "helper/invariants.spec";

// 2. for all a, released[a] <= (totalReceived * shares[a] ) // totalShares

// Passa ma vedilo meglio comunque

rule released_leq_total_received{

    requireInvariant shares_sum_eq_totalShares();
    requireInvariant released_sum_totalReleased();

    env e;
    uint index;
    address addr = getPayee(index);

    uint addrReleased = getReleased(addr);
    uint addrShares = getShares(addr);

    mathint bal = getBalance();
    mathint totalReleased = getTotalReleased();
    mathint totalReceived = bal + totalReleased;
    mathint totalShares = getTotalShares();

    // require addrShares > 0;
    // require totalShares >= addrShares;
    // require totalReleased >= addrReleased;

    // addrReleased is assigned by CVL without following the rules of release(), so it has
    // values that are not necessarily equal to the sum of the shares released
    // adding the
    // require addrReleased <= totalReceived * addrShares / totalShares;

    assert( addrReleased <= totalReceived * addrShares / totalShares); 
}