class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        Find the maximum water a container can store.

        The container is formed by two vertical lines and the x-axis.
        Water stored = distance between lines × height of shorter line.

        Approach: Two Pointer O(n)
            - Start from both ends
            - Calculate area at each step
            - Move the shorter pointer inward

        Args:
            height (list[int]): List of vertical line heights.

        Returns:
            int: Maximum water the container can store.

        Example:
            >>> s = Solution()
            >>> s.maxArea([1,8,6,2,5,4,8,3,7])
            49
            >>> s.maxArea([1,1])
            1

        Time Complexity:  O(n) - single pass
        Space Complexity: O(1) - no extra space
        """
        max_area = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area