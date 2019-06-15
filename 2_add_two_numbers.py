'''
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def printListNode(head):
    while (head):
        print head.val
        head = head.next

node11 = ListNode(2)
node12 = ListNode(4)
node13 = ListNode(6)
node11.next = node12
node12.next = node13

node21 = ListNode(5)
node22 = ListNode(6)
node23 = ListNode(4)
node21.next = node22
node22.next = node23
print "test"

p1 = node11
p2 = node21
ret = p = ListNode(0)
c = 0
while (p1 or p2):
    sum = c
    if p1:
        sum += p1.val
        p1 = p1.next
    if p2:
        sum += p2.val
        p2 = p2.next
    p.next = ListNode(sum % 10)
    p = p.next

    c = sum / 10

if c > 0:
    p.next = ListNode(sum % 10)

printListNode(ret.next)

