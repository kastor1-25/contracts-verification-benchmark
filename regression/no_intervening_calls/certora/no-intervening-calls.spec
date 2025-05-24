methods {
    function f() external envfree;
}
rule no_intervening_calls {
	env e;
	require (currentContract.b);
    f();
    f(); 
    assert (currentContract.b);
}