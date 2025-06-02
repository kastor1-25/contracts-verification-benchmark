import "helper/methods.spec";


// If you call release twice in a row, the second call should revert

rule release_release_revert {
    env e1; 
    uint index;
    
    address addr = getPayee(index);

    require getShares(addr) > 0;
    
    require releasable(addr) > 0;
    mathint released = releasable(addr);

    mathint balanceBefore = getBalance();

    release@withrevert(e1, addr);
    require !lastReverted;

    mathint balanceAfter = getBalance();
    // Forces CVL to not assume that release() caused a trasnaction to this contract
    require balanceAfter == balanceBefore - released; 

    release@withrevert(e1,addr);
    bool reverted = lastReverted;
    
    assert reverted;
}

// TODO
/* 
the rule seems to be useless, since we cant really ensure that nothing happens in between the calls
Is there a way to assure the consecutive execution of the two releases?
*/

/*
invariant shares_gt_zero(address account)
    getShares(account) > 0
    { preserved release(address a) with (env e){
        require a != 0;
    } }*/