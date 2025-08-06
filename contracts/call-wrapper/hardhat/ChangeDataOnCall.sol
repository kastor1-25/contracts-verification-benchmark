pragma solidity >= 0.8.2;

contract ChangeDataOnCall {
    fallback() external {
        msg.sender.call(abi.encodeWithSignature("modifystorage(uint256)", 1));
    }
}