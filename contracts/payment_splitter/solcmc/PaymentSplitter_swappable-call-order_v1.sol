// SPDX-License-Identifier: MIT
// OpenZeppelin Contracts (last updated v4.8.0) (finance/PaymentSplitter.sol)

pragma solidity ^0.8.0;

/// @custom:version conformant to specification

contract PaymentSplitter {

    uint256 private totalShares;
    uint256 private totalReleased;

    mapping(address => uint256) private shares;
    mapping(address => uint256) private released;
    address[] private payees;
    
    constructor(address[] memory payees_, uint256[] memory shares_) payable {
        require(payees_.length == shares_.length, "PaymentSplitter: payees and shares length mismatch");
        require(payees_.length > 0, "PaymentSplitter: no payees");

        for (uint256 i = 0; i < payees_.length; i++) {
            addPayee(payees_[i], shares_[i]);
        }
    }

    receive() external payable virtual { }

    function releasable(address account) public view returns (uint256) {
        uint256 totalReceived = address(this).balance + totalReleased;
        return pendingPayment(account, totalReceived, released[account]);
    }

    function release(address payable account) public virtual {
        require(shares[account] > 0, "PaymentSplitter: account has no shares");

        uint256 payment = releasable(account);

        require(payment != 0, "PaymentSplitter: account is not due payment");

        // totalReleased is the sum of all values in released.
        // If "totalReleased += payment" does not overflow, then "released[account] += payment" cannot overflow.
        totalReleased += payment;
        unchecked {
            released[account] += payment;
        }

        (bool success,) = account.call{value: payment}("");
        require(success);
    }

    function pendingPayment(
        address account,
        uint256 totalReceived,
        uint256 alreadyReleased
    ) private view returns (uint256) {
        return (totalReceived * shares[account]) / totalShares - alreadyReleased;
    }

    function addPayee(address account, uint256 shares_) private {
        require(account != address(0), "PaymentSplitter: account is the zero address");
        require(shares_ > 0, "PaymentSplitter: shares are 0");
        require(shares[account] == 0, "PaymentSplitter: account already has shares");

        payees.push(account);
        shares[account] = shares_;
        totalShares = totalShares + shares_;
    }

    
    function invariant(uint index1, uint index2) public view{
        require (index1 < payees.length);
        require (index2 < payees.length);
        require (index1 != index2);

        address payee_1 = payees[index1];
        address payee_2 = payees[index2];

        
    }   
}

/*

rule swappable_call_order {
    requireInvariant shares_sum_eq_totalShares();
    requireInvariant released_sum_totalReleased();

    env e;

    uint index1;
    uint index2;

    require index1 != index2;
    
    require index1 < currentContract.payees.length;
    require index2 < currentContract.payees.length;

    address addr1 = currentContract.payees[index1];
    address addr2 = currentContract.payees[index2];

    storage initial = lastStorage;

    release(e, addr1);
    release(e, addr2);
    storage final1 = lastStorage;

    release(e, addr2) at initial;
    release(e, addr1);
    storage final2 = lastStorage;
    assert final1 == final2;
}

 */