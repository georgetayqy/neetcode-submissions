# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        result = ListNode()
        result_traverser = result

        while head != None:
            head_node, first_node = None, None
            has_met_requirement = True

            for i in range(k):
                if head is None:
                    has_met_requirement = False
                    break

                if i == 0:
                    latest_node = head
                
                main_next_in_line = head.next
                head.next = first_node
                first_node = head
                head = main_next_in_line
            
            if not has_met_requirement:
                print("TOO SHORT!")
                head_of_list = first_node
                new_head = None
                first_node_of_new_list = None

                while head_of_list:
                    if not first_node_of_new_list:
                        first_node_of_new_list = head_of_list

                    next_head_of_list = head_of_list.next
                    head_of_list.next = new_head
                    new_head = head_of_list
                    head_of_list = next_head_of_list
                
                first_node = new_head
                latest_node = first_node_of_new_list

            result_traverser.next = first_node
            result_traverser = latest_node


            # DEBUG CODE
            # traverser = first_node
            # while traverser:
            #     print(traverser.val)
            #     traverser = traverser.next
            # END DEBUG CODE

        return result.next
