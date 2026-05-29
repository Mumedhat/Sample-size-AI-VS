from app.agents.consensus import weighted_vote

def test_weighted_vote_zero_total():
    # Test items where the confidence total evaluates to zero
    items = [("A", 0.0), ("B", 0.0)]
    res, conf = weighted_vote(items)
    assert res is None
    assert conf == 0.0

def test_weighted_vote_normal():
    items = [("A", 0.8), ("A", 0.6), ("B", 0.4)]
    res, conf = weighted_vote(items)
    assert res == "A"
    assert conf > 0
