from collections import deque
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Create nodes

def solve(root):
    q = deque()
    if root != None:
        q.appendleft(root)
    min_sum = float('inf')
    while len(q) != 0:
        curr_sum = 0
        n = len(q)
        for i in range(n):
            curr_sum += q[0].val
            if q[0].left != None:
                q.append(q[0].left)
            if q[0].right != None:
                q.append(q[0].right)
            q.popleft()
        
        min_sum = min(min_sum, curr_sum)
    return min_sum

root = Node(9)
root.left = Node(1)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(2)

print(solve(root))