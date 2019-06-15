'''
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

from util import ListNode, printListNode

#class ListNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.next = None
#
#def printListNode(head):
#    while (head):
#        print head.val
#        head = head.next

node11 = ListNode(2)
node12 = ListNode(4)
node13 = ListNode(6)
node11.next = node12
node12.next = node13

'''
1: pre, 2(p)->4->6
    1.1: 2(p)->4(tmp)->6
    1.2: None(pre)<-2(p)  4->6
    1.3: None<-2(prev/p)  4->6
    1.4: None<-2(pre)  4(p)->6

2: None<-2(prev) 4(p)->6
    2.1: None<-2(prev)  4(p)->6(tmp)
    2.2: None<-2(prev)<-4(p)  6(tmp)
    2.3: None<-2<-4(prev/p)  6
    2.4: None<-2<-4(prev)  6(p)
...
'''

p = node11
pre = None
while (p):
    # keep NEXT STEP into tmp
    tmp = p.next
    p.next = pre
    pre = p
    p = tmp

printListNode(pre)

