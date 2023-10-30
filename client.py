from src.binary_node import Node
from src.min_heap import MinHeapListImpl

def inorder_traversal(node: Node) -> None:
    if node == None:
        return

    inorder_traversal(node.left)
    print(node.value)
    inorder_traversal(node.right)


def level_order_traversal(root: Node) -> None:
    if root == None:
        return

    queue = [root]
    while(len(queue) > 0):
        i = len(queue)

        while(i):   
            node = queue.pop(0)
            print(node.value)
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
            i -= 1
        print('-' * 20)
    
def get_last_node(root: Node) -> Node:
    queue = [root]
    j = 0

    while(j < len(queue)):
        i = len(queue) - j

        while(i <= len(queue) - j):
            node = queue[j]
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
            i += 1
            j += 1
    return queue.pop()


if __name__ == '__main__':
    # # Let's create a simple complete tree
    # root = Node(1)
    # root.left = Node(2)
    # root.right = Node(3)
    # root.left.left = Node(4)
    # root.left.right = Node(5)
    # root.right.left = Node(6)
    # root.right.right = Node(7)


    # # inorder_traversal(root)
    # # level_order_traversal(root)

    # last_node = get_last_node(root)
    # print(last_node)

    # Operations

    heap = MinHeapListImpl()
    while True:
        print('Option 1: Insert')
        print('Option 2: Get min')
        print('Option 3: To Stop')
        option = int(input('Enter your option: '))
        
        if option == 1:
            value = int(input('Inter value: '))
            heap.insert(value)
            
        elif option == 2:
            print('Min value is: ', heap.get_min())

        else:
            break

    try:
        print('Printing remaining values in the heap: ', end='')
        while True:
            print(heap.get_min(), end=' ')
    except:
        pass
        





















