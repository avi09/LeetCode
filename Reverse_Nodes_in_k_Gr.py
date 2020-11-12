# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not ListNode:
            return None

        def get_node(node, n):
                x = node
                for i in range(n):
                    if x.next:
                        x = x.next
                return x

        def sw_value(node, x1, x2):
            x_1 = get_node(node, x1)
            x_2 = get_node(node, x2-1)
            if x2-x1==1:
                tm = int(x_1.val)
                x_1.val = x_2.val
                x_2.val = tm
            else:
                tm = []
                for i in range(x1, x2):
                    tm.append(get_node(node, i).val)
                tm = tm[::-1]
                for i in range(x1, x2):
                    get_node(node, i).val = tm[i-x1]
            return node
        
        n = 0
        while get_node(head, n).next:
            n+=1
            
        for i in range(0, n+1, k):
            if (n-i+1)>=k:
                print(i, i+k)
                head = sw_value(head, i, i+k)
            
        return head
