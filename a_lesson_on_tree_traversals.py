#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2022-04-14
##


# BFS
# 1. Recursive Approach: is complex, requiring discovery and tracking
# 2. Iterative Approach: is simple because you read first value as you traverse
queue = collections.deque([root])
while queue:
    node = queue.popleft()
    if node.left: queue.append(node.left)
    if node.right: queue.append(node.right)
    print(node.val) # Do an action as you traverse BFS here



# DFS Preorder
# 1. Recursive Approach: is simple
traversal = []
def traverse(root):
    if root:
        traversal.append(root.val)
        traverse(root.left)
        traverse(root.right)
traverse(root)
return traversal

# 2. Iterative Approach: is simple because you read last value as you traverse
if root is None: return []
output = []
stack = [root]
while stack:
    root = stack.pop()
    if root:
        output.append(root.val) # here is the action
        if root.right: stack.append(root.right)
        if root.left: stack.append(root.left)
return output



# DFS Inorder
# 1. Recursive Approach:
traversal = []
def traverse(tree):
    if tree:
        traverse(tree.left)
        traversal.append(tree.val) # here is the action
        traverse(tree.right)
traverse(root)
return traversal

# 2. Iterative Approach: is complex because you have to control order of stack
stack = []
traversal = []
current = root
while True:
    if current:
        stack.append(current)
        current = current.left
    elif(stack):
        current = stack.pop()
        traversal.append(current.val)
        current = current.right
    else:
        break
return traversal



# DFS Postorder
# 1. Recursive Approach:
traversal = []
def traverse(root):
    if root:
        traverse(root.left)
        traverse(root.right)
        traversal.append(root.val) # here is the action
traverse(root)
return traversal
# 2. Iterative Approach: very painful to resolve stack order not worth it
