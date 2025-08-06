pragma solidity >= 0.8.2;

contract SelfDestructOnCall {

    constructor() payable {}
    fallback() external payable {
        selfdestruct(payable(msg.sender));
    }
}