// SPDX-License-Identifier: MIT
pragma solidity >=0.8.2;

import "./Crowdfund_v1.sol";

contract RevertOnReceive {
    Crowdfund public crowdfund;

    constructor() payable {}

    receive() external payable {
        revert("RevertOnReceive: receive reverted");
    }

    function setCrowdfund(address _crowdfund) external {
        crowdfund = Crowdfund(_crowdfund);
    }

    function donate() external payable {
        crowdfund.donate{value: msg.value}();
    }

    function reclaim() external {
        crowdfund.reclaim();
    }

    function withdraw() external {
        crowdfund.withdraw();
    }
}
