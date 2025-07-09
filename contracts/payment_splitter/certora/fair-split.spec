import "helper/methods.spec";
import "helper/invariants.spec";

// for all a, released[a] <= (totalReceived * shares[a] ) // totalShares

/* rule fair_split{

    requireInvariant shares_sum_eq_totalShares();
    requireInvariant released_sum_totalReleased();
    requireInvariant payee_shares_gt_zero();
    
    env e;
    uint index;

    require forall address addr .
        currentContract.released[addr] == 0;
    

/*     require currentContract.payees.length < 4;
 *//*    require index < currentContract.payees.length;
    address addr = currentContract.payees[index];

    uint addrReleased = getReleased(addr);
    uint addrShares = getShares(addr);

    mathint totalReceived = getBalance() + currentContract.totalReleased;

    require totalReceived < 2^255; // to avoid overflow in the division

    uint bal = getBalance();
    assert addrReleased <= totalReceived * currentContract.shares[addr] / currentContract.totalShares;
} */

invariant fair_split (uint index)
    
    index < currentContract.getPayeesLength() => 
    
    getReleased(currentContract.payees[index]) <= (
        (getBalance() + currentContract.totalReleased) * 
        currentContract.shares[currentContract.payees[index]] /
        currentContract.totalShares
    ) 
    {
        preserved {
            requireInvariant shares_sum_eq_totalShares();
            requireInvariant released_sum_totalReleased();
            requireInvariant payee_shares_gt_zero();
        }

/*         preserved addPayee(address a, uint shares_) with (env e){
            requireInvariant shares_sum_eq_totalShares();
            requireInvariant released_sum_totalReleased();
            requireInvariant payee_shares_gt_zero();

            require currentContract.payees.length < 3;
            require currentContract.totalReleased == 0;

            require forall address addr .
                currentContract.released[addr] == 0;

        } */
    }
