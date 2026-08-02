# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        previous_group = dummy

        while True:
            # retrieve the kth group
            k_th_group = self.getK(previous_group, k)
            if not k_th_group:
                break
            
            # reverse the current group
            next_group = k_th_group.next
            previous, curr = k_th_group.next, previous_group.next

            # reverse until we reach the starting node of the next group
            while curr != next_group:
                next_part = curr.next
                curr.next = previous
                previous = curr
                curr = next_part
            
            # temp is the first node in the group
            temp = previous_group.next
            previous_group.next = k_th_group
            previous_group = temp
        
        return dummy.next

    def getK(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1
        
        return node
