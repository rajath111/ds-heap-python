from typing import Any
from src.heap_base import HeapBase

class MaxHeap(HeapBase):
    def insert(self, value):
        self._list.append(value)
        self._last += 1

        # Adjust the value by swap
        i = self._last
        parent = self._parent(i)

        while i > 0 and self._list[i] > self._list[parent]:
            self._swap(i, parent)
            i = parent
            parent = self._parent(i)
        

    def get_max(self) -> Any:
        assert self._last >= 0, 'cannot call get_max when heap is empty'
        max_val = self._list[0]

        self._list[0] = self._list[self._last]
        self._last -= 1
        self._list.pop()

        # Swap till, all the children are lesser
        i = 0
        left = self._left(i)
        right = self._right(i)

        while i < self._last and (left <= self._last and self._list[left] > self._list[i]) or (right <= self._last and self._list[right] > self._list[i]):
            swap_index = None
            if right < self._last and self._list[right] > self._list[left]:
                swap_index = right
            else:
                swap_index = left

            self._swap(i, swap_index)
            i = swap_index
            left = self._left(i)
            right = self._right(i)

        return max_val

