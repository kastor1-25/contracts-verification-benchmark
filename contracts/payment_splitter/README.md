# Payment Splitter

## Specification
This contract allows to split Ether payments among a group of accounts. The sender does not need to be aware that the Ether will be split in this way, since it is handled transparently by the contract.

The split can be in equal parts or in any other arbitrary proportion. The way this is specified is by assigning each account to a number of shares. Of all the Ether that this contract receives, each account will then be able to claim an amount proportional to the percentage of total shares they were assigned. The distribution of shares is set at the time of contract deployment and can't be updated thereafter.

 `PaymentSplitter` follows a pull payment model. This means that payments are not automatically forwarded to the accounts but kept in this contract, and the actual transfer is triggered as a separate step by calling the release() function.

## Properties
- **non-zero-payees**:  for all accounts `a` in `payees`, `a != address(0)`.
- **positive-shares**:  for all addresses `addr` in `payees`, `shares[addr] > 0`.
- **releasable-balance-check**:  for all addresses `addr` in `payees`, `releasable(addr)` is less than or equal to the balance of the contract.
- **releasable-sum-balance**:  the sum of the releasable funds for every accounts is equal to the balance of the contract.
- **zero-shares-fail**:  if `payees[0] == addr` then `shares[addr] == 0` (should fail).

## Versions
- **v1**: conformant to specification

## Ground truth
|        | non-zero-payees          | positive-shares          | releasable-balance-check | releasable-sum-balance   | zero-shares-fail         |
|--------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|
| **v1** | 1                        | 1                        | 1                        | 1                        | 0                        |
 

## Experiments
### SolCMC
#### Z3
|        | non-zero-payees          | positive-shares          | releasable-balance-check | releasable-sum-balance   | zero-shares-fail         |
|--------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|
| **v1** | UNK                      | FN!                      | UNK                      | FN                       | TN                       |
 

#### ELD
|        | non-zero-payees          | positive-shares          | releasable-balance-check | releasable-sum-balance   | zero-shares-fail         |
|--------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|
| **v1** | ERR                      | ERR                      | ERR                      | ERR                      | ERR                      |
 


### Certora
|        | non-zero-payees          | positive-shares          | releasable-balance-check | releasable-sum-balance   | zero-shares-fail         |
|--------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|
| **v1** | ERR                      | FN                       | FN                       | FN                       | TN                       |
 

