# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        # Function to reverse a linked list
        def reverseLinkedList(node):
            prev = None
            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node
            return prev
        
        # Function to get the middle of the linked list
        def getMiddle(node):
            slow = fast = node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        # Function to compare two linked lists
        def compareLists(list1, list2):
            while list1 and list2:
                if list1.val != list2.val:
                    return False
                list1 = list1.next
                list2 = list2.next
            return True
        
        # Get the middle of the linked list
        middle = getMiddle(head)
        
        # Reverse the second half of the linked list
        second_half_reversed = reverseLinkedList(middle)
        
        # Compare the first and second halves of the linked list
        return compareLists(head, second_half_reversed)
