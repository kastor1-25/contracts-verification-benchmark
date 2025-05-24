# Double Call

## Specification


## Properties
- **double-call**: b

## Ground truth
|        | double-call |
|--------|-------------|
| **v1** | 1[^1]       |
 
[^1]: Subsequent calls should be atomic and nothing should happen in between

## Experiments
### SolCMC
#### Z3
|        | double-call |
|--------|-------------|
| **v1** | TP!         |
 

#### ELD
|        | double-call |
|--------|-------------|
| **v1** | TP!         |
 


### Certora
|        | double-call |
|--------|-------------|
| **v1** | FN          |
 

