from src.binary_node import Node
from src.max_heap import MaxHeap


if __name__ == '__main__':
    # # Let's create a simple complete tree

    heap = MaxHeap()
    heap.insert(10)
    heap.insert(23)
    heap.insert(5)

    # assert heap.get_max() == 23

    heap.insert(100)
    heap.insert(12)
    heap.insert(200)
    print('started')
    while True:
        print(heap.get_max(), end=' ')




















