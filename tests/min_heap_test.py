import sys
import os
sys.path.append(os.path.sep.join(__file__.split(os.path.sep)[:-2]))
from src.min_heap import MinHeapListImpl

def common_test():
    heap = MinHeapListImpl()

    heap.insert(10)
    heap.insert(30)
    heap.insert(1)
    heap.insert(10092)
    heap.insert(329)
    heap.insert(20)

    assert heap.get_min() == 1
    assert heap.get_min() == 10
    assert heap.get_min() == 20
    assert heap.get_min() == 30
    assert heap.get_min() == 329
    assert heap.get_min() == 10092


def border_test():
    heap = MinHeapListImpl()

    heap.insert(10000)
    assert heap.get_min() == 10000


def empty_test():
    heap = MinHeapListImpl()
    assert heap.get_min()