from typing import Any
from src.binary_node import Node

class MinHeap:

    def __init__(self) -> None:
        self._root = None
        self._last = None

    def insert(self, value: Any) -> None:
        if self._root == None:
            self._root = Node(value=value)

        else:
            # Insert at last location
            
            # Do swaps recursively
            pass

    def _insert_last(self) -> Node:
        pass

    def get_min(self) -> Any:
        pass