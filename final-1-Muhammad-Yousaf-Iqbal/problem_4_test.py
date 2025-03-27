from problem_4 import *

def test_ONS_insert():
    ons = OrderedNodeSequence()
    for n in range(10,0,-2):
        ons.insert(n)
    for n in range(1,10,2):
        ons.insert(n)
    assert repr(ons) == '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'

def test_ONS_empty():
    ons = OrderedNodeSequence()
    assert ons.is_empty()
    ons.insert(1)
    assert not ons.is_empty()

def test_ONS_peek():
    ons = OrderedNodeSequence()
    assert not ons.peek()
    ons.insert(1)
    assert ons.peek() == 1

def test_ONS_contains():
    ons = OrderedNodeSequence()
    assert not ons.contains(1)
    for n in range(1,10,2):
        ons.insert(n)
    assert ons.contains(5)

def test_ONS_remove():
    ons = OrderedNodeSequence()
    for i in range(10):
        ons.insert(i)
    assert not ons.remove(20)
    count = 1
    assert ons.remove(5)
    while not ons.is_empty() and count < 100:
        ons.remove(ons.peek())
        count += 1
    assert repr(ons) == '[]'

# def test_ONS_remove_100():
#     ons = OrderedNodeSequence()
    assert not ons.remove(2)
    ons.insert(1)
    assert not ons.remove(2)

