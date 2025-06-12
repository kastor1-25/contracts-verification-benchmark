import "helper/methods.spec";
import "helper/invariants.spec";


// Im not sure if this is using too many assumption
rule positive_shares {
    requireInvariant shares_sum_eq_totalShares();
    require currentContract.totalShares > 0;

    uint index;
    address payee = getPayee(index);
    assert getShares(payee) > 0;
}


/*
Notare che senza la `require currentContract.totalShares > 0;` il test fallisce, probabile
che il Prover abbia difficoltà a verificare require presenti nel costruttore

TODO review this assumption

se si omette la regola, assegna comunque un singolo payee ma con shares = 0
*/