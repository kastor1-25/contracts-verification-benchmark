// SPDX-License-Identifier: MIT
// OpenZeppelin Contracts (last updated v4.8.0) (finance/PaymentSplitter.sol)

pragma solidity ^0.8.0;

/// @custom:version conformant to specification

contract PaymentSplitter {

    uint256 private constant PAYEES = 3;
    address private owner;
    uint256 private numPayees = 0;

    uint256 private totalShares;
    uint256 private totalReleased;

    mapping(address => uint256) private shares;
    mapping(address => uint256) private released;
    address[] private payees;
    
/*     constructor(address[] memory payees_, uint256[] memory shares_) payable {
        owner = msg.sender;

        require(payees_.length == shares_.length, "PaymentSplitter: payees and shares length mismatch");
        require(payees_.length > 0, "PaymentSplitter: no payees");
        require (payees_.length <= PAYEES, "PaymentSplitter: too many payees");

        addPayee(payees_[0], shares_[0]);
        addPayee(payees_[1], shares_[1]);
        addPayee(payees_[2], shares_[2]);
    } 
 */
    constructor (address payee1, uint256 shares1, address payee2, uint256 shares2, address payee3, uint256 shares3) payable {
        owner = msg.sender;

        require(numPayees < PAYEES);
        addPayee(payee1, shares1);
        addPayee(payee2, shares2);
        addPayee(payee3, shares3);
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

        require(numPayees < PAYEES);
        require(owner == msg.sender, "PaymentSplitter: only owner can add payees");
        
        require(account != address(0), "PaymentSplitter: account is the zero address");
        require(shares_ > 0, "PaymentSplitter: shares are 0");
        require(shares[account] == 0, "PaymentSplitter: account already has shares");

        payees.push(account);
        shares[account] = shares_;
        totalShares = totalShares + shares_;
        numPayees+=1;
    }
    //positive-shares invariant
    function invariant(uint index) public view {
        require(index < payees.length, "Index out of bounds");
        assert(shares[payees[index]] > 0);
    }
}

