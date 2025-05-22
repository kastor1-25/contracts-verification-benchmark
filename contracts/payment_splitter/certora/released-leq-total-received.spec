import "helper/methods.spec";

// 2. for all a, released[a] <= (totalReceived * shares[a] ) // totalShares

rule released_leq_total_received{
    env e;

    uint index;
    address addr = getPayee(index);

    uint addrReleased = getReleased(addr);
    uint addrShares = getShares(addr);
    mathint bal = getBalance();
    mathint totalReleased = getTotalReleased();
    
    mathint totalReceived = bal + totalReleased;

    mathint totalShares = getTotalShares();

    require totalShares >= addrShares;
    require totalReleased >= addrReleased;

    assert( addrReleased <= totalReceived * addrShares / totalShares);
}