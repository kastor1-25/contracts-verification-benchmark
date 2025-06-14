# Payment Splitter

## Specification
This contract allows to split Ether payments among a group of accounts. The sender does not need to be aware that the Ether will be split in this way, since it is handled transparently by the contract.

The split can be in equal parts or in any other arbitrary proportion. The way this is specified is by assigning each account to a number of shares. Of all the Ether that this contract receives, each account will then be able to claim an amount proportional to the percentage of total shares they were assigned. The distribution of shares is set at the time of contract deployment and can't be updated thereafter.

 `PaymentSplitter` follows a pull payment model. This means that payments are not automatically forwarded to the accounts but kept in this contract, and the actual transfer is triggered as a separate step by calling the release() function.

## Properties
- **funds-get-transfered**: for all accounts `a` in `payees`, if `releasable(a) > 0`, then `release(a)` does not revert.
- **non-zero-payees**:  for all accounts `a` in `payees`, `a != address(0)`.
- **positive-shares**:  for all addresses `addr` in `payees`, `shares[addr] > 0`.
- **releasable-balance-check**:  for all addresses `addr` in `payees`, `releasable(addr)` is less than or equal to the balance of the contract.
- **releasable-sum-balance**:  the sum of the releasable funds for every accounts is equal to the balance of the contract.
- **release-release-revert**: two consecutive calls to `release` for the same account `a` should revert on the second call.
- **released-leq-total-received**: the total amount released to all accounts should be less than or equal to the total amount received by the contract.

## Versions
- **v1**: conformant to specification

## Ground truth
|        | funds-get-transfered        | non-zero-payees             | positive-shares             | releasable-balance-check    | releasable-sum-balance      | release-release-revert      | released-leq-total-received |
|--------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|
| **v1** | 0                           | 1                           | 1                           | 1                           | 1                           | 1                           | 1                           |
 

## Experiments
### SolCMC
#### Z3
|        | funds-get-transfered        | non-zero-payees             | positive-shares             | releasable-balance-check    | releasable-sum-balance      | release-release-revert      | released-leq-total-received |
|--------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|
| **v1** | TN                          | UNK                         | FN!                         | UNK                         | FN                          | UNK                         | FN!                         |
 

#### ELD
|        | funds-get-transfered        | non-zero-payees             | positive-shares             | releasable-balance-check    | releasable-sum-balance      | release-release-revert      | released-leq-total-received |
|--------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|
| **v1** | UNK                         | UNK                         | UNK                         | UNK                         | UNK                         | UNK                         | UNK                         |
 


### Certora
|        | funds-get-transfered        | non-zero-payees             | positive-shares             | releasable-balance-check    | releasable-sum-balance      | release-release-revert      | released-leq-total-received |
|--------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|
| **v1** | TN                          | FN                          | TP!                         | TP!                         | TP!                         | TP!                         | TP!                         |
 

