class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Find the longest palindromic substring in a given string.

        A palindrome is a string that reads the same forward and backward.

        Approach:
        - Generate all possible substrings using two nested loops.
        - Check each substring if it is a palindrome by reversing it.
        - Track the longest palindrome found.

        Time Complexity:
        - O(n^3)
          (n^2 substrings * O(n) palindrome check)

        Space Complexity:
        - O(1) (ignoring output string)

        Example:
        Input: "bacbacacaca"
        Output: "acacaca"
        """

        longest = ""  # Stores the longest palindrome found

        # Generate all substrings
        for i in range(len(s)):
            for j in range(i, len(s)):
                current = s[i:j+1]  # Extract substring

                # Check if substring is a palindrome
                if current == current[::-1]:
                    # Update longest if current is longer
                    if len(current) > len(longest):
                        longest = current

        return longest


# Example usage
obj1 = Solution()
print(obj1.longestPalindrome("bacbacacaca"))