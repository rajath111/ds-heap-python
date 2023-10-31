class HeapBase:
    def __init__(self) -> None:
        self._list = []
        self._last: int = -1

    def _parent(self, i: int) -> int:
        return int((i - 1) / 2)

    def _left(self, i: int) -> int:
        return (i * 2) + 1

    def _right(self, i: int) -> int:
        return (i * 2) + 2 

    def _swap(self, i: int, j: int) -> None:
        temp = self._list[i]
        self._list[i] = self._list[j]
        self._list[j] = temp