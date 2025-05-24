rule double_call {
	env e;
	require (currentContract.b);

    f(e);
    bool B = currentContract.b;
    
    assert (currentContract.b);
}