# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # we can use 2 pointers at the start of the list, and offset
        # the right pointer by n units ahead
        # that way we can ensure that the distance between the left
        # and the right pointer is n, meaning that the left pointer
        # is actually the node we want to delete

        # however, because we need to delete the left pointer,
        # instead, we should track the node BEFORE the left pointer
        # to do so, we use a dummy node at the start of the list
        # and set it such that the next item of the dummy node is the
        # true start of the list
        
        # the right pointer should start at the actual start/head of the list
        # to account for this (before left pointer) behaviour

        dummy = ListNode(next=head)
        left = dummy
        right = head

        # maintain seperation between the left and right pointer
        # to width of n (or)
        for i in range(n):
            right = right.next
        
        # then, we shift both forward in tandem so that we can
        # maintain the space between the pointers to be n
        # the node that l is 
        #    [1, 2, 3, 4], n = 1
        #  l     r
        #     l     r
        #        l     r
        #           l     r [exceeds]
        while right:
            left = left.next
            right = right.next
        
        # we set the next link of left to the next of the next of
        # the left node to skip the next node (deleting the node)
        left.next = left.next.next

        # dummy is the 
        return dummy.next
