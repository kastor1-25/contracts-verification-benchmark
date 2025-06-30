import "helper/methods.spec";
import "helper/invariants.spec";

rule positive_shares {
    requireInvariant shares_sum_eq_totalShares();
    requireInvariant payee_shares_gt_zero();
    
    uint index;
    address payee = getPayee(index);
    assert getShares(payee) > 0;
}


/*
Notare che senza la `require currentContract.totalShares > 0;` contenuta nell'invariant il test fallisce, probabile
che il Prover abbia difficoltà a verificare require presenti nel costruttore

TODO review this assumption

se si omette la regola, assegna comunque un singolo payee ma con shares = 0
*/