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



# BFS Problem Example, Checking for Symmetrical Trees
# Start by confirming that there are two leafs from start, else return appropriately
# Create a deque, it could be a stack too, each pair is okay on it's own, can pop left or right
# Check if the left and right mirror out for each pair, append a new pair if possible
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not (root.left and root.right):
            if (root.left or root.right): return False
            return True
        queue = collections.deque([[root.left, root.right]])

        while queue:
            left, right = queue.popleft()
            if left.val != right.val: return False
            if left.left or right.right:
                if left.left and right.right:
                    queue.append([left.left,right.right])
                else: return False
            if left.right or right.left:
                if left.right and right.left:
                    queue.append([right.left,left.right])
                else: return False
        return True
