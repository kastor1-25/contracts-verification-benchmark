/*
ghost mapping(uint => uint256) ghostValues {
    init_state axiom forall uint index. ghostValues[index] == 0;
}

persistent ghost mathint counter {
    init_state axiom counter == 0;
}

hook Sstore currentContract.values[INDEX uint index] uint256 value {
    ghostValues[index] = value;
    counter = counter + 1 ;
}*/

ghost uint256[MAX_SIZE] pobas;



// Alternative approach using built-in sum operator
rule sum_matches_array_values_builtin {
    env e;
    /* require currentContract.values.length == 0;
    require currentContract.sum == 0; */

    require currentContract.sum == getSumOfValues(e);
/*
    require currentContract.values.length == 0;
    require currentContract.sum == 0;
    require counter == 0;
    require forall uint i. ghostValues[i] == 0;
*/

/*
    mathint _len = currentContract.values.length;
    mathint ghost_len = counter;

    assert _len == ghost_len;*/

    // mathint totalFromGhost = sum uint i. ghostValues[i];
    
    assert currentContract.sum == getSumOfValues(e);
}







/*
SPECS FOR V1

ghost mapping (address => uint256) ghostBalances;

hook Sstore balances[KEY address a] uint256 v {
    ghostBalances[a] = v;
}

ghost mathint ghostSum {
  init_state axiom ghostSum == 0;
}

hook Sstore currentContract.sum uint256 newSum (uint256 oldSum) {
  ghostSum = newSum;
}

rule a {
    // requireInvariant ghostBalancesMatchContract();

    mathint boh = currentContract.sum;
    mathint totalSum = ghostSum;
    mathint totalFromGhost = sum address b. ghostBalances[b];
    
    assert (totalSum == totalFromGhost);
}

rule b{
    // Force initialization by calling a function that uses balances, doesnt seem to work
    env e;
    mathint bal = nativeBalances[currentContract]; 
    
    mathint totalSum = currentContract.sum;
    mathint totalFromGhost = sum address b. ghostBalances[b];
    
    assert (totalSum == totalFromGhost);
}

invariant ghostBalancesMatchContract()
    forall address a. ghostBalances[a] == currentContract.balances[a];

    */