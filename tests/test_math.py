from src.math import add,sub

def test_add():
    assert add(2,3)==5
    assert add(2,-2)==0
    assert add(-4,2)==-2

def test_sub():
    assert sub(2,3)==-1
    assert sub(2,-2)==4
    assert sub(-4,2)==-6