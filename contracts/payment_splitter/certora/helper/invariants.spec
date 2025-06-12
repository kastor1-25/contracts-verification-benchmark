import "methods.spec";

invariant shares_sum_eq_totalShares()
    getSumOfShares() == currentContract.totalShares && currentContract.totalShares > 0;

invariant released_sum_totalReleased()
    getSumOfReleased() == currentContract.totalReleased;