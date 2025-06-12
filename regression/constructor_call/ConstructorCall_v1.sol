// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract ConstructorCall {
    uint256 private sum;

    uint256[] private values;
    
    constructor(uint256[] memory _values) {
        require(_values.length > 0);
        
        for (uint256 i = 0; i < _values.length; i++) {
            doSum(_values[i]);
        }
    }

    function doSum(uint256 _value) public {

        require(_value > 0);
        
        sum += _value;
        values.push(_value) ;
    }

    function doNothing() public {
        // This function does nothing
    }

    function getSumOfValues() public view returns (uint256) {
        uint256 total = 0;
        for (uint256 i = 0; i < values.length; i++) {
            total += values[i];
        }
        return total;
    }
}


/* 
contract V1

contract ConstructorCall {
    uint256 private sum;

    mapping(address => uint256) private balances;
    
    constructor(address[] memory _addresses ,uint256[] memory _values) {
        require(_addresses.length == _values.length);
        require(_addresses.length > 0);
        
        for (uint256 i = 0; i < _values.length; i++) {
            doSum(_addresses[i],_values[i]);
        }
    }


    function doSum(address _addr, uint256 _value) private {

        require(_addr != address(0));
        require(_value > 0);
        require(balances[_addr] == 0);
        
        sum += _value;
        balances[_addr] = _value;
    }
}
*/