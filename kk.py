# --------------------------------------------------
# LeetCode Problem 1044: Longest Duplicate Substring
# --------------------------------------------------
# Description:
# Given a string s, return the longest substring of s that appears 
# at least twice. The two occurrences may overlap.
#
# If no such substring exists, return an empty string "".
#
# -------------------------------------------------------------
# Examples:
# Example 1:
#   Input:  s = "banana"
#   Output: "ana"
#
# Example 2:
#   Input:  s = "abcd"
#   Output: ""
#
# -------------------------------------------------------------
# Constraints:
#   2 <= len(s) <= 3 * 10^4
#   s consists of lowercase English letters.
# -------------------------------------------------------------
# Approach Used: Rolling Hash + Binary Search
# -------------------------------------------------------------
# Idea:
# - We are asked to find the longest substring that repeats.
# - Observation: if there is a duplicate substring of length L,
#   there must be one of length < L too.
#   → This means we can apply **binary search** on the length L.
#
# - For each candidate length L:
#     1. Compute rolling hashes of all substrings of length L.
#     2. Use a hash set to check for collisions (duplicate hash values).
#     3. Use modulo arithmetic to prevent overflow.
#
# - Continue binary searching until we find the largest L with a duplicate.
#
# Key Algorithmic Tools:
#   • Binary Search → O(log n)
#   • Rolling Hash (Rabin–Karp) → O(n)
#
# Overall Time Complexity:  O(n log n)
# Space Complexity:         O(n)
# -------------------------------------------------------------


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        import random

        n = len(s)
        # Map characters to integers: a → 0, b → 1, ..., z → 25
        nums = [ord(c) - ord('a') for c in s]

        # Choose a large random base and modulus for hashing
        base = random.randint(26, 100)
        mod = 2**63 - 1  # Large prime-like modulus

        # Helper function to search for duplicate substring of given length
        def search(L: int) -> int:
            """Return starting index of duplicate substring of length L, else -1."""
            h = 0
            for i in range(L):
                h = (h * base + nums[i]) % mod
            seen = {h}

            # Precompute base^L % mod
            baseL = pow(base, L, mod)

            for start in range(1, n - L + 1):
                # Rolling hash update: remove left char, add new right char
                h = (h * base - nums[start - 1] * baseL + nums[start + L - 1]) % mod
                if h in seen:
                    return start
                seen.add(h)
            return -1

        # Binary search on substring length
        left, right = 1, n
        start = -1

        while left <= right:
            mid = (left + right) // 2
            idx = search(mid)
            if idx != -1:
                # Found duplicate of length mid → try longer
                left = mid + 1
                start = idx
            else:
                right = mid - 1

        # Return the substring using final found length
        L = left - 1
        return s[start:start + L] if start != -1 else ""

sol = Solution()
# -------------------------------------------------------------
# Example Runs (uncomment to test)
# -------------------------------------------------------------

# print(sol.longestDupSubstring("banana"))  # Output: "ana"
# print(sol.longestDupSubstring("abcd"))    # Output: ""
# print(sol.longestDupSubstring("aaaaa"))   # Output: "aaaa"
