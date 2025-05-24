# No Intervening Calls

## Specification
The `NoInterveningCalls` contract manages a boolean state variable `b` with two functions:

- `f()`: A no-op function that performs no state changes.
- `g()`: A function that modifies the state by setting `b` to `false`.

## Properties
- **no-intervening-calls**: No additional or intervening function calls are allowed between the specified function calls within a CVL rule.

## Ground truth
|        | no-intervening-calls |
|--------|----------------------|
| **v1** | 1                    |
 

## Experiments
### SolCMC
#### Z3
|        | no-intervening-calls |
|--------|----------------------|
| **v1** | TP!                  |
 

#### ELD
|        | no-intervening-calls |
|--------|----------------------|
| **v1** | TP!                  |
 


### Certora
|        | no-intervening-calls |
|--------|----------------------|
| **v1** | TP!                  |
 

