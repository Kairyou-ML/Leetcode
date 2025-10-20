# -------------------------------------------------------------
# LeetCode Problem: Integer to English Words
# -------------------------------------------------------------
# Description:
# Convert a non-negative integer num to its English words representation.
#
# -------------------------------------------------------------
# Examples:
# Example 1:
#   Input:  num = 123
#   Output: "One Hundred Twenty Three"
#
# Example 2:
#   Input:  num = 12345
#   Output: "Twelve Thousand Three Hundred Forty Five"
#
# Example 3:
#   Input:  num = 1234567
#   Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
#
# Example 4:
#   Input:  num = 0
#   Output: "Zero"
#
# -------------------------------------------------------------
# Constraints:
#   0 <= num <= 2^31 - 1
#
# -------------------------------------------------------------
# Approach Used: Recursive Divide & Map (Readable & Efficient)
# -------------------------------------------------------------
# Idea:
# - Break the number into groups of three digits: Billion, Million, Thousand, Hundred.
# - Convert each 3-digit group into words using helper function.
# - Skip groups that are zero.
#
# Example:
#   1,234,567 -> ["One Million", "Two Hundred Thirty Four Thousand", "Five Hundred Sixty Seven"]
#
# Time Complexity:  O(1)   (since num is bounded by 2^31 - 1)
# Space Complexity: O(1)
# -------------------------------------------------------------


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        # Dictionaries for word mapping
        below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
                    "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
                    "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty",
                "Sixty", "Seventy", "Eighty", "Ninety"]

        thousands = ["", "Thousand", "Million", "Billion"]

        # Helper function to convert numbers < 1000
        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return below_20[n] + " "
            elif n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            else:
                return below_20[n // 100] + " Hundred " + helper(n % 100)

        res = ""
        i = 0  # thousand group index

        # Process each group of 3 digits
        while num > 0:
            if num % 1000 != 0:
                res = helper(num % 1000) + thousands[i] + " " + res
            num //= 1000
            i += 1

        # Strip extra spaces
        return res.strip()


# --------------------------------
# sol = Solution()
# print(sol.numberToWords(123))          # "One Hundred Twenty Three"
# print(sol.numberToWords(12345))        # "Twelve Thousand Three Hundred Forty Five"
# print(sol.numberToWords(1234567))      # "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# print(sol.numberToWords(0))            # "Zero"
