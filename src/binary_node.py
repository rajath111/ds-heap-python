class Node:

    def __init__(self, value: any, parent: 'Node' = None, left: 'Node' = None, right: 'Node' = None) -> None:
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


    def __str__(self) -> str:
        return f'Node(value={self.value})'