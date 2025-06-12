import "helper/methods.spec";
import "helper/invariants.spec";


// if i have n shares and the balance is n+1
rule releasable_sum_balance {
    requireInvariant shares_sum_eq_totalShares();
    
    
    mathint releasable = getTotalReleasable(); // maybe move this to a ghost variable
    mathint balance = getBalance();

    assert getTotalReleasable() == getBalance();
}


/* 

this has become an invariant

rule released_sum_totalReleased { // released_sum_eq_totalReleased
    mathint totalReleased = currentContract.totalReleased;

    mathint payeesReleasedSum = sum address a . payeesReleased[a];

    assert payeesReleasedSum == totalReleased;
}

invariant  */




/* ghost mapping (address => uint256) payeesShares;

hook Sstore shares[KEY address a] uint256 value{
    payeesShares[a] = value;
} */
/*
rule shares_sum_eq_totalShares {

    mathint totalShares = currentContract.totalShares;

    mathint payeesShareSum = sum address a. payeesShares[a]; 


    // require payeesShareSum == totalShares; // this rule seems useless
    assert payeesShareSum == totalShares;
}*/



