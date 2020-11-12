# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        def get_val(node, n) -> int:
            x = node
            for i in range(n):
                if x.next:
                    x = x.next
            return x.val

        def get_valid(node, n) -> bool:
            x = node
            for i in range(n):
                if x.next:
                    x = x.next
                else:
                    return False
            return True

        def insert(answer, val):
            if not answer.next:
                answer.next = ListNode(val)
            else:
                ref = answer.next
                while ref.next:
                    ref = ref.next
                ref.next = ListNode(val)
            return answer

        lists = [x for x in lists if x is not None]

        if not lists:
            return None

        new = []
        n = len(lists)

        for i in range(n):
            x = 0
            while True:
                if get_valid(lists[i], x):
                    new.append(get_val(lists[i], x))
                    x+=1
                else:
                    break
        print(new)
