methods {
    function approve_payment() external;
    function refund() external; 
    function open_dispute() external;
    function arbitrate(address) external;
    function redeem() external;
    function getBalance() external returns (uint256) envfree;
    function getBuyer() external returns (address) envfree;
    function getSeller() external returns (address) envfree;
    function getArbiter() external returns (address) envfree;
    function getState() external returns (Escrow.State) envfree;
    function getFee() external returns (uint256) envfree;
    function getDeposit() external returns (uint256) envfree;
}

rule always_reachable_redeem {

    env e;
    method f;
    method g;
    calldataarg args1;
    calldataarg args2;

    require
        (  f.selector == sig:approve_payment().selector
        || f.selector == sig:refund().selector
        || f.selector == sig:open_dispute().selector
        || f.selector == sig:arbitrate(address).selector
        || f.selector == sig:redeem().selector);
        

    require getState() == Escrow.State.AGREE;

    f(e, args1); // approve/refund or dispute

    assert getState() == Escrow.State.REDEEM || getState() == Escrow.State.DISPUTE;

    require
        ( getState() == Escrow.State.REDEEM && (
            g.selector == sig:redeem().selector
        ) 
        || getState() == Escrow.State.DISPUTE && (
            g.selector == sig:arbitrate(address).selector
        ));

    g(e, args2);

    assert getState() == Escrow.State.REDEEM || getState() == Escrow.State.END;
}


/* 
if (getState(e) == Escrow.State.Redeem) {
    g.selector = sig:redeem().selector;
}
else if (getState(e) == Escrow.State.Dispute) {
    g.selector = sig:arbitrate(address).selector;
}
*/