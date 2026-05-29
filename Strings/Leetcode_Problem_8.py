class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Convert a string to a 32-bit signed integer (like C/C++ atoi).

        Algorithm Steps:
        1. Ignore leading whitespace.
        2. Check for an optional '+' or '-' sign.
        3. Read digits and build the number until a non-digit is found.
        4. Clamp the result within the 32-bit signed integer range:
           [-2^31, 2^31 - 1].
        5. Return the final integer.

        Notes:
        - Leading zeros are handled automatically during number construction.
        - If no valid digits are found, return 0.
        - Overflow is handled BEFORE it happens.
        """

        # Step 1: Remove leading whitespace
        s = s.lstrip()

        # Edge case: if string becomes empty
        if not s:
            return 0

        # Step 2: Determine sign
        sign = 1
        index = 0

        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1

        # Step 3: Convert digits to integer
        result = 0

        # 32-bit signed integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        while index < len(s) and s[index].isdigit():
            digit = int(s[index])

            # Step 4: Check for overflow BEFORE updating result
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            # Build the number
            result = result * 10 + digit
            index += 1

        # Step 5: Apply sign and return result
        return sign * result