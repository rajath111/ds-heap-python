# Heap Data structure using List and Tree

Heap is a data structure which returns maximum / minimum value from collection of data on O(log n). Average time complexity of both insertion and retrival is O(log n).  
There are two variants of heap.

    1. Min Heap - Returns min value from the container

    2. Max Heap - Returns max value from the container


Lets consider Min heap for explanation,
At any node, both children values will be greater than or equal to the current node value.

## Implementation of Min heap using List/Array
As heap is complete binary tree, we can represent it using linear data structre like array. Lets define some rules.

For any node i, its left and right children are at:  
```
left -> (i * 2) + 1  
right -> (i * 2) + 2
```

For any node i, its parent can be found at:  
```    
parent -> (i - 1) / 2
```
1. It always stores min/max value at the root element.

2. Insertion happen at the last node position. If the value is lesser than its parent, then swap with parent. Do this recursively.

3. Deletion/Retrival happen from root and last element is made as root element

4. If the value is greater than any of its children, swap with the smallest child, Do this recursively.


## Test the result
I have added tests for both MinHeap and MaxHeap. 
Run below command from root folder to execute the tests:
```
python tests\test_runner.py
```

Or you can import the classes and test them. Also use them.

## Extra things learnt while doing this implementation
1. Importing python module from different folder
   ```
    import sys
    import os
    sys.path.append(os.path.sep.join(__file__.split(os.path.sep)[:-2]))
    from src.min_heap import MinHeap
   ```


2. Load python module from file - Runtime
   ```
    from types import FunctionType, ModuleType
    from os import path, listdir
    from importlib.util import spec_from_file_location, module_from_spec

    module_name = module_path.split(path.sep)[-1][:-3]  # Provide a custom name for the module
    spec = spec_from_file_location(module_name, module_path)
    custom_module = module_from_spec(spec)
    spec.loader.exec_module(custom_module)
   ```