# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # Boundary check
        if not headA or not headB:
            return None
            
        pointerA = headA
        pointerB = headB
        
        # Loop continues until the two pointers meet
        while pointerA != pointerB:
            # If pointerA reaches the end of list A, redirect it to head of list B
            # Otherwise, just move it to the next node
            pointerA = pointerA.next if pointerA else headB
            
            # If pointerB reaches the end of list B, redirect it to head of list A
            # Otherwise, just move it to the next node
            pointerB = pointerB.next if pointerB else headA
            
        # Either they met at the intersection node, or both are None (no intersection)
        return pointerA