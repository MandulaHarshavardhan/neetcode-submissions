"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dici={None:None}
        cur=head
        while cur:
            copy=Node(cur.val)
            dici[cur]=copy
            cur=cur.next
        cur=head
        while cur:
            copy=dici[cur]
            copy.next=dici[cur.next]
            copy.random=dici[cur.random]
            cur=cur.next
        return dici[head]