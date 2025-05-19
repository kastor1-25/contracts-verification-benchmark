import "helper/methods.spec";

// TODO: valuta se ha senso quando cambiata o semplicemente levarla

rule release_insufficient_revert {
    uint index;
    address addr = getPayee(index);
    require addr != address(0);
    require getShares(addr) > 0;

    uint r = getTotalReleasable();

    
}