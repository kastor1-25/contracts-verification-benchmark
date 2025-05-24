pragma solidity ^0.8.25;

contract NoInterveningCalls {
	bool private b = true;

    function f() public{}

    function g() public {
        b = false;
    }

    function h() public {
        require(b);
        f();
        f();
        assert(b);
    }
}