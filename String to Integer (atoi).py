# ---------------------------
# String to Integer (atoi)
# ---------------------------
# Description:
# Implement the function myAtoi(string s), which converts a string
# into a 32-bit signed integer (similar to the C/C++ atoi function).
#
# Conversion Rules:
# 1. Skip all leading whitespace.
# 2. Read an optional '+' or '-' sign.
# 3. Read digits continuously and convert them into an integer.
# 4. Stop reading at the first non-digit character.
#
# Overflow Rules:
# - If the value exceeds the 32-bit signed integer range:
#       Return  2_147_483_647   (INT_MAX)
#       Return -2_147_483_648   (INT_MIN)
#
# If no valid conversion can be performed, return 0.
#
# -------------------------------------------------------------
# Examples:
# Example 1:
#   Input:  s = "42"
#   Output: 42
#
# Example 2:
#   Input:  s = "   -42"
#   Output: -42
#
# Example 3:
#   Input:  s = "4193 with words"
#   Output: 4193
#
# Example 4:
#   Input:  s = "words and 987"
#   Output: 0
#
# Example 5:
#   Input:  s = "-91283472332"
#   Output: -2147483648   # Clamped to INT_MIN
#
# -------------------------------------------------------------
# Constraints:
#   0 <= len(s) <= 200
#   s may contain letters, digits, spaces, and symbols.
# -------------------------------------------------------------
# Approach Used: String Parsing + Implementation
# -------------------------------------------------------------
# Idea:
# - Move through the string while skipping leading whitespace.
# - Determine the sign of the number.
# - Read digit characters and form the number.
# - Apply 32-bit overflow clamping during accumulation.
#
# Key Points:
#   • No need for complex parsing logic.
#   • Must check overflow before multiplying and adding digits.
#
# Overall Time Complexity:  O(n)
# Space Complexity:         O(1)
# -------------------------------------------------------------


class Solution:
    def myAtoi(self, s: str) -> int:

        INT_MAX = 2_147_483_647
        INT_MIN = -2_147_483_648

        i = 0
        n = len(s)

        # 1. Skip leading spaces
        while i < n and s[i] == " ":
            i += 1

        # 2. Read sign
        sign = 1
        if i < n and s[i] in ["+", "-"]:
            sign = -1 if s[i] == "-" else 1
            i += 1

        # 3. Convert digits
        result = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord("0")

            # Overflow check before multiplying
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return result * sign

sol = Solution()
# -------------------------------------------------------------
# Example Runs (uncomment to test)
# -------------------------------------------------------------
# print(sol.myAtoi("42"))              # 42
# print(sol.myAtoi("   -42"))          # -42
# print(sol.myAtoi("4193 with words")) # 4193
# print(sol.myAtoi("words and 987"))   # 0
# print(sol.myAtoi("-91283472332"))    # -2147483648
