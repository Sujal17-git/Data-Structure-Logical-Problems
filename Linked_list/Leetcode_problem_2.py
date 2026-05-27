class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        Add two numbers represented by linked lists.

        Each linked list stores digits in reverse order.
        Each node contains a single digit.

        Example:
        l1 = 2 → 4 → 3  (represents 342)
        l2 = 5 → 6 → 4  (represents 465)

        Output:
        7 → 0 → 8  (represents 807)

        Approach:
        - Traverse both linked lists
        - Add corresponding digits along with carry
        - Store result digit in a new linked list
        - Continue until both lists and carry are exhausted

        Time Complexity: O(max(n, m))
        Space Complexity: O(max(n, m))
        """

        # Dummy node to simplify result list creation
        dummy = ListNode(0)

        # Pointer to build the new list
        current = dummy

        # Carry to store overflow (e.g., 10 → carry 1)
        carry = 0

        # Traverse both lists until all values and carry are processed
        while l1 or l2 or carry:

            # Get values from current nodes (0 if node is None)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Add values along with carry
            total = val1 + val2 + carry

            # Update carry (tens place)
            carry = total // 10

            # Extract digit (ones place)
            digit = total % 10

            # Create new node with the digit and attach to result list
            current.next = ListNode(digit)

            # Move current pointer forward
            current = current.next

            # Move l1 and l2 pointers forward if possible
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Return the result list (skip dummy node)
        return dummy.next