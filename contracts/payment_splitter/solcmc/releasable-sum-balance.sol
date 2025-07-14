// releasable-sum-balance invariant 
function invariant() public view {
    uint _total_releasable = 0;
    for (uint i = 0; i < payees.length; i++) {
        _total_releasable += releasable(payees[i]);
    }

    assert(_total_releasable == address(this).balance);
}