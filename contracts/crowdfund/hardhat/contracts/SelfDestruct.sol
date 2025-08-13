pragma solidity >=0.8.2;

import "./Crowdfund_v1.sol";

contract SelfDestruct {
    Crowdfund public crowdfund;
    constructor() payable {}

    function setCrowdfund(address _crowdfund) external {
        crowdfund = Crowdfund(_crowdfund);
    }

    function selfDestruct() external {
        // Self-destruct the contract, sending any remaining balance to the crowdfund contract
        selfdestruct(payable(address(crowdfund)));
    }
}