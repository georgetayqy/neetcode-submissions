# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        else:
            # save the reversed portion of the list
            reversed = head

            # if the head.next is not None, meaning that there are more
            # list to reverse
            if head.next is not None:
                # we reverse the back portion of the list first
                reversed = self.reverseList(head.next)

                # we then set the next of the next node of the head to the head
                # this reverses the list
                # h -> x -> ...
                # h.next = x
                # h.next.next = x->
                # head.next.next = head => h -> x
                #                          ^    |
                #                          |    |
                #                          ------
                head.next.next = head
            
            # we then need to set the head.next to None, since we want to break the link
            # set up in the recursion above
            # head.next.next = head => h -> None    x
            #                          ^            |
            #                          |            |
            #                          --------------
            # result is: x -> h -> None (reversed!)
            head.next = None

            return reversed
