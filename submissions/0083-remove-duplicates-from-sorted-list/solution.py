# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
            
        trail = head
        lead = trail.next
        while True:
            if lead and lead.val == trail.val:
                lead = lead.next
            else:
                if trail.next != lead:
                    trail.next = lead
                trail = lead
                if not lead:
                    break
                lead = lead.next
        return head
