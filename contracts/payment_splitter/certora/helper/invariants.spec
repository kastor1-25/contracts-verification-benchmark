import "methods.spec";

/*
Notare che senza la `require currentContract.totalShares > 0;` contenuta nell'invariant il test fallisce, probabile
che il Prover abbia difficoltà a verificare require presenti nel costruttore
*/
invariant shares_sum_eq_totalShares()
    getSumOfShares() == currentContract.totalShares && currentContract.totalShares > 0;

invariant released_sum_totalReleased()
    getSumOfReleased() == currentContract.totalReleased;