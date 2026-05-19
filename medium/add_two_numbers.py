from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        num1 = 0
        num2 = 0
        cur_result = 0
        carry = 0
        dummy = ListNode(0)
        current = dummy
        while l1 or l2 or carry > 0:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            cur_result = num1 + num2 + carry
            if cur_result >= 10:
                carry = 1
            else:
                carry = 0
            new_node = ListNode(cur_result % 10)
            current.next = new_node

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            current = current.next

        return dummy.next


if __name__ == "__main__":
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))

    sol = Solution()
    res = sol.addTwoNumbers(l1, l2)

    print("Result linked list: ", end="")
    while res:
        print(res.val, end=" -> " if res.next else "\n")
        res = res.next
