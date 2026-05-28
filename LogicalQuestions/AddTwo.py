# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :type rtype: Optional[ListNode]
        """
        # Create a dummy node to easily construct the return list
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Loop as long as there are nodes to process or a carry remaining
        while l1 or l2 or carry:
            # Get values from current nodes if they exist, else 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate total sum for this position and the new carry
            total = val1 + val2 + carry
            carry = total // 10
            out_val = total % 10
            
            # Create the new node and advance the result pointer
            current.next = ListNode(out_val)
            current = current.next
            
            # Move to the next nodes in the input lists if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        return dummy.next