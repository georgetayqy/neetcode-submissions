# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # find middle and sever the connection
        just_before, middle = self.findMiddle(head)
        just_before.next = None

        # reverse
        middle = self.reverse(middle)
        
        # weave the lists together
        self.zip(head, middle)

    def zip(self, ls1, ls2):
        if not ls1:
            return ls2
        
        if not ls2:
            return ls1
        
        dummy_node = ListNode()

        while ls1 and ls2:
            print(ls1.val, ls2.val)
            ls1_next = ls1.next
            ls2_next = ls2.next

            dummy_node.next = ls1
            ls1.next = None
            ls1 = ls1_next
            dummy_node = dummy_node.next

            dummy_node.next = ls2
            ls2.next = None
            ls2 = ls2_next
            dummy_node = dummy_node.next

        if ls1:
            dummy_node.next = ls1
        elif ls2:
            dummy_node.next = ls2
        
        return dummy_node.next
    
    def reverse(self, head):
        tail, curr = None, head

        while curr:
            # save a reference to the next item in the list
            next_in_line = curr.next

            # reset the next pointer to point at previous to reverse
            # the chain
            curr.next = tail

            # set previous to current to advance the list
            tail = curr

            # then set curr to the rest of the list
            curr = next_in_line
        
        # this is the reversed list
        return tail

    
    def findMiddle(self, head):
        previous, curr, nxt = None, head, head.next

        while curr and nxt:
            previous = curr
            curr = curr.next
            nxt = nxt.next

            if nxt:
                nxt = nxt.next
        
        return previous, curr
