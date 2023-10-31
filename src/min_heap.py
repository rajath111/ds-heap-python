from typing import Any
from src.heap_base import HeapBase

class MinHeap(HeapBase):
    '''
        So the value of any node will be less than their children.
    '''

    def insert(self, value: Any) -> None:
        #  Insert at the last location + 1
        self._list.append(value)
        self._last += 1

        # Recursively adjust 
        # Compare with its parent, if parent is lesser then swap
        i = self._last

        # End condition - i greater than root
        while(i > 0 and self._list[self._parent(i)] > self._list[i]):
            self._swap(self._parent(i), i)
            i = self._parent(i)
    
    def get_min(self) -> Any:
        assert self._last >= 0, 'There should be atlest one element in the heap to call get_min'
        # Remove the first element
        result = self._list[0]

        # Store last element in root position
        self._list[0] = self._list[self._last]
        self._last -= 1
        self._list.pop()

        # Swap with the lowest child recursively
        i = 0
        left = self._left(i)
        right = self._right(i)

        # End condition i less than the last element
        while i < self._last and (left <= self._last and self._list[left] < self._list[i]) or (right <= self._last and self._list[right] < self._list[i]):
            swap_index = None
            if(right < self._last and self._list[right] < self._list[left]):
                swap_index = right
            else:
                swap_index = left

            self._swap(i, swap_index)
            i = swap_index
            left = self._left(i)
            right = self._right(i)

        return result
