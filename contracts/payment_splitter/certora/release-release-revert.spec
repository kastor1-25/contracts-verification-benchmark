import "helper/methods.spec";

rule release_release_revert {
    env e1; 
    uint index;
    
    address addr = getPayee(index);
    require releasable(addr) > 0;
    mathint release = releasable(addr);

    mathint balanceBefore = getBalance();

    release@withrevert(e1, addr);
    require !lastReverted;

    release@withrevert(e1,addr);
    bool reverted = lastReverted;

    mathint balanceAfter = getBalance();
    assert(reverted && balanceAfter+release == balanceBefore); 

    
}

// TODO
/* 
the rule seems to be useless, since we cant really ensure that nothing happens in between the calls
Is there a way to assure the consecutive execution of the two releases? prolly not my nigga
*/