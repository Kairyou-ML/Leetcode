# -------------------------------------------------
# Find the Closest Palindrome
# -------------------------------------------------
# Description:
# Given a string n representing an integer, return the closest 
# integer (in absolute difference) that is a palindrome.
#
# If there is a tie, return the smaller one.
#
# A palindrome number reads the same backward as forward.
#
# -------------------------------------------------------------
# Examples:
# Example 1:
#   Input:  n = "123"
#   Output: "121"
#
# Example 2:
#   Input:  n = "1"
#   Output: "0"
#   Explanation: The closest palindrome is 0 since 0 and 2 are both 1 away,
#                but 0 is smaller.
#
# Example 3:
#   Input:  n = "99"
#   Output: "101"
#
# -------------------------------------------------------------
# Constraints:
#   - n consists of digits only
#   - 1 <= n.length <= 18
#   - n does not have leading zeros (except for "0" itself)
# -------------------------------------------------------------
# Approach Used: Prefix Mirroring + Boundary Handling
# -------------------------------------------------------------
# Idea:
# - To find the closest palindrome, consider candidates formed by:
#     1. Lower palindrome near the prefix
#     2. Higher palindrome near the prefix
#     3. Edge cases (like 999 -> 1001, 1000 -> 999)
#
# Steps:
#   1. Take the first half of the string (prefix).
#   2. Generate palindromes by mirroring the prefix, prefix+1, and prefix-1.
#   3. Add edge cases:
#       • "1000...0" -> "999...9"
#       • "999...9"  -> "1000...001"
#   4. Compare all candidates (absolute difference) to n.
#   5. Return the smallest in case of tie.
#
# Time Complexity:  O(1)  (since number length ≤ 18, fixed)
# Space Complexity: O(1)
# -------------------------------------------------------------


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        num = int(n)

        # Edge cases for boundaries (like 1000, 999)
        candidates = {
            10**length + 1,          # e.g., 999 -> 1001
            10**(length - 1) - 1     # e.g., 1000 -> 999
        }

        # Extract prefix (first half + middle if odd)
        prefix = int(n[:(length + 1) // 2])

        # Generate palindromes by mirroring prefix-1, prefix, prefix+1
        for diff in (-1, 0, 1):
            new_prefix = str(prefix + diff)
            if length % 2 == 0:
                palindrome = int(new_prefix + new_prefix[::-1])
            else:
                palindrome = int(new_prefix + new_prefix[:-1][::-1])
            candidates.add(palindrome)

        # Remove the number itself (since we want *closest different* palindrome)
        candidates.discard(num)

        # Find closest by absolute difference, then smallest if tie
        return str(min(candidates, key=lambda x: (abs(x - num), x)))

sol = Solution()
# --------------------------------
# Example Runs (uncomment to test)
# --------------------------------

# print(sol.nearestPalindromic("123"))   # Output: "121"
# print(sol.nearestPalindromic("1"))     # Output: "0"
# print(sol.nearestPalindromic("99"))    # Output: "101"
# print(sol.nearestPalindromic("1000"))  # Output: "999"
# print(sol.nearestPalindromic("807045053224792883"))  # Large case
