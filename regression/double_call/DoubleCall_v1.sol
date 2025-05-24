pragma solidity ^0.8.25;


contract DoubleCall {
	bool private b = true;

    function f() public{
        
    }

    function g() public {
        b = false;
    }

}