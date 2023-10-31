from src.max_heap import MaxHeap

if __name__ == '__main__':
    # Using Max heap to sort array in descending order
    heap = MaxHeap()
    heap.insert(10)
    heap.insert(23)
    heap.insert(5)

    heap.insert(100)
    heap.insert(12)
    heap.insert(200)
    while True:
        try:
            print(heap.get_max(), end=' ')
        except:
            break




















