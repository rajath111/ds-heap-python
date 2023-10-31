import sys
import os
sys.path.append(os.path.sep.join(__file__.split(os.path.sep)[:-2]))
from src.max_heap import MaxHeap

def complete_test():
    heap = MaxHeap()

    heap.insert(10)
    heap.insert(23)
    heap.insert(5)

    assert heap.get_max() == 23

    heap.insert(100)
    heap.insert(12)
    heap.insert(200)

    assert heap.get_max() == 200, 'Expected 200'
    assert heap.get_max() == 100, 'Expected 100'
    assert heap.get_max() == 12, 'Expected 12'
    assert heap.get_max() == 10, 'Expected 10'
    assert heap.get_max() == 5, 'Expected 5'


def border_test():
    heap = MaxHeap()

    heap.insert(10)

    assert heap.get_max() == 10


def empty_test():
    heap = MaxHeap()

    assert heap.get_max()

