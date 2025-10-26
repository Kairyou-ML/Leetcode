# -------------------------------------------------------------
# LeetCode Problem: Longest Substring Without Repeating Characters
# -------------------------------------------------------------
# Description:
# Given a string s, find the length of the longest substring 
# without repeating characters.
#
# A substring is a contiguous sequence of characters within a string.
#
# -------------------------------------------------------------
# Examples:
# Example 1:
#   Input:  s = "abcabcbb"
#   Output: 3
#   Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
#   Input:  s = "bbbbb"
#   Output: 1
#   Explanation: The answer is "b", with the length of 1.
#
# Example 3:
#   Input:  s = "pwwkew"
#   Output: 3
#   Explanation: The answer is "wke", with the length of 3.
#                Notice that "pwke" is a subsequence, not a substring.
#
# Example 4:
#   Input:  s = ""
#   Output: 0
#
# -------------------------------------------------------------
# Constraints:
#   0 <= len(s) <= 5 * 10^4
#   s consists of English letters, digits, symbols, and spaces.
# -------------------------------------------------------------
# Approach Used: Sliding Window + HashMap
# -------------------------------------------------------------
# Idea:
# - Use two pointers (left and right) to define a sliding window.
# - Use a hash map (dictionary) to track the last seen index of each character.
# - Move the right pointer across the string:
#     • If the current character is already in the window, 
#       move the left pointer to skip the duplicate.
#     • Always update the longest substring length.
#
# Time Complexity:  O(n)
# Space Complexity: O(min(n, charset_size))  (≈ O(n))
# -------------------------------------------------------------


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store the last index of each character
        last_seen = {}
        left = 0     # Left boundary of current window
        max_len = 0  # Maximum length found

        for right, ch in enumerate(s):
            # If the character is repeated and inside current window
            if ch in last_seen and last_seen[ch] >= left:
                # Move left pointer to one position after the duplicate
                left = last_seen[ch] + 1
            
            # Update the last seen position of current character
            last_seen[ch] = right

            # Calculate the current window length
            max_len = max(max_len, right - left + 1)

        return max_len

sol = Solution()

# -------------------------------------------------------------
# Example Runs (uncomment to test)
# -------------------------------------------------------------

# print(sol.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
# print(sol.lengthOfLongestSubstring("bbbbb"))     # Output: 1
# print(sol.lengthOfLongestSubstring("pwwkew"))    # Output: 3
# print(sol.lengthOfLongestSubstring(""))          # Output: 0
