# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle, stored in slow
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # the slow pointer is always 1 before the middle node
        # so we break the link and advance to the next node
        # to get the position for the right half of the list
        copy_reference_for_slow = slow.next
        slow.next = None

        # the dummy node acts as the head of the reversed list
        # so while iterating, we need to reverse the links
        # in the reversed list and point it towards this dummy link
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
        # do not need a dummy node to interleave, just use the inherent
        # pointers available in the first and second lists to do this
        # head -> next, next -> head.next
        # but save head.next and next.next to advance the interleaving
        # to the next 2 nodes
        first, second = head, dummy_node

        while second is not None:
            # we need the next pointers as we will be breaking
            # the links
            next_one, next_two = first.next, second.next

            # a -> b -> c,    e -> d
            # a -> e,  set to ->b -> c, ->d
            first.next, second.next = second, next_one

            # advance the pointers here
            first, second = next_one, next_two
