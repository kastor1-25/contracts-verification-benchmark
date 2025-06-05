import "helper/methods.spec";


// if i have n shares and the balance is n+1
rule releasable_sum_balance {
    mathint releasable = getTotalReleasable(); // maybe move this to a ghost variable
    mathint balance = getBalance();

    assert getTotalReleasable() == getBalance();
}






ghost mapping (address => uint256) payeesShares;

hook Sstore shares[KEY address a] uint256 value{
    payeesShares[a] = value;
}

rule shares_sum_eq_totalShares {

    mathint totalShares = currentContract.totalShares;

    mathint payeesShareSum = sum address a. payeesShares[a]; 


    // require payeesShareSum == totalShares; // this rule seems useless
    assert payeesShareSum == totalShares;
}



ghost mapping (address => uint256) payeesReleased;

hook Sstore released[KEY address a] uint256 value{
    payeesReleased[a] = value;
}

rule released_sum_totalReleased { // released_sum_eq_totalReleased
    mathint totalReleased = currentContract.totalReleased;

    mathint payeesReleasedSum = sum address a . payeesReleased[a];

    // require payeesReleasedSum == totalReleased; // this rule seems useless
    assert payeesReleasedSum == totalReleased;
}
