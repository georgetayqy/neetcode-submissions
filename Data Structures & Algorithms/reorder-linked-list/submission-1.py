# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle, stored in slow
        slow, fast = head, head

        while slow is not None and fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        copy_reference_for_slow = slow.next
        slow.next = None

        # form the list in reverse, set to None
        dummy_node = None

        # 4 -> 3 -> 2 -> 1
        # D -> 1 -> 2 -> 3 -> 4                

        # while the iterator pointer is not None
        # we do the following
        # 1. copy a reference to the next node in the iterator pointer
        #    this is the next item we want to reverse
        # 2. sever the link between the current iterator pointer node
        #    with the next node
        # 3. move the dummy node reference forward. the dummy node reference
        #    always point to the head of the new reversed list
        # 4. set the iterator pointer variable to the next node stored in 
        #    step 1
        while copy_reference_for_slow is not None:
            next_node_to_reverse = copy_reference_for_slow.next
            copy_reference_for_slow.next = dummy_node
            dummy_node = copy_reference_for_slow
            copy_reference_for_slow = next_node_to_reverse

        # interleave the lists
        interleaved = ListNode()
        new_head = interleaved

        while dummy_node is not None:
            next_one = head.next
            next_two = dummy_node.next

            head.next = dummy_node
            dummy_node.next = next_one

            head = next_one
            dummy_node = next_two