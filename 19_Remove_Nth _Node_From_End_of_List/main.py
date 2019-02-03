class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        while head:
            print(head.val)
            head = head.next

        return 0
        
solution  = Solution()
test_list = [1,2,3,4,5]

head = ListNode(test_list[0])
tail= head

for i in range(1, len(test_list)):
    tail.next = ListNode(test_list[i])
    tail.next = tail
    

print(solution.removeNthFromEnd(head, 2))