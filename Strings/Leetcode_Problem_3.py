class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Find the length of the longest substring without repeating characters.

        Approach:
        - Use a sliding window (implemented using a list).
        - Iterate through each character in the string.
        - If a duplicate character is found:
            remove characters from the left until the duplicate is removed.
        - Keep updating the maximum substring found so far.

        Example:
        Input: "abcabcbb"
        Output: 3  (substring: "abc")

        Time Complexity:
        - O(n^2) due to pop(0) operation (removing from front of list)

        Space Complexity:
        - O(n) for storing substring
        """

        # This list stores the current substring (window) with unique characters
        longest_sub_string = []

        # This stores the longest substring found so far
        max_return = ""

        # Iterate through each character in the input string
        for char in s:

            # If the character is already in current substring → duplicate found
            if char in longest_sub_string:

                # Remove characters from the left until duplicate is gone
                while char in longest_sub_string:
                    longest_sub_string.pop(0)  # remove first element (left side)

            # Add current character to substring
            longest_sub_string.append(char)

            # Update maximum substring if current is longer
            if len(longest_sub_string) > len(max_return):
                max_return = "".join(longest_sub_string)

        # Return length of longest substring
        return len(max_return)