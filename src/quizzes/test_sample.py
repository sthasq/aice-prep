def accuracy(y_true, y_pred):
    assert len(y_true) == len(y_pred) and len(y_true) > 0
    return sum(int(a==b) for a,b in zip(y_true, y_pred)) / len(y_true)

def test_accuracy_basic():
    assert accuracy([1,0,1,1], [1,1,1,0]) == 0.5

def test_accuracy_all_correct():
    assert accuracy([1,1,1], [1,1,1]) == 1.0

def test_accuracy_all_wrong():
    assert accuracy([0,0], [1,1]) == 0.0