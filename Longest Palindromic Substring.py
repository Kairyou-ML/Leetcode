# -------------------------------------------------------------
# LeetCode Problem: Longest Palindromic Substring
# -------------------------------------------------------------
# Description:
# Given a string s, return the longest palindromic substring in s.
#
# A palindrome is a string that reads the same backward as forward.
# For example:
#   "aba" is a palindrome, but "abc" is not.
#
# -------------------------------------------------------------
# Examples:
# Example 1:
#   Input:  s = "babad"
#   Output: "bab"
#   Explanation: "aba" is also a valid answer.
#
# Example 2:
#   Input:  s = "cbbd"
#   Output: "bb"
#
# -------------------------------------------------------------
# Constraints:
#   1 <= s.length <= 1000
#   s consists of only digits and English letters.
#
# -------------------------------------------------------------
# Follow-up:
#   Can you solve it in O(n²) time and O(1) space?
#
# -------------------------------------------------------------
# Approaches:
# 1. Expand Around Center (Recommended)
#    - Time complexity: O(n²)
#    - Space complexity: O(1)
#
# 2. Dynamic Programming
#    - Time complexity: O(n²)
#    - Space complexity: O(n²)
#
# 3. Manacher's Algorithm (Advanced)
#    - Time complexity: O(n)
#    - Space complexity: O(n)
# -------------------------------------------------------------


def longestPalindrome(s: str) -> str:
    """
    Return the longest palindromic substring in s.
    """

    def expand_from_center(left: int, right: int) -> str:
        # While pointers are within bounds and characters match, expand
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1   
            right += 1  
        
        return s[left + 1:right]

    # Edge case: empty string
    if not s:
        return ""

    longest = ""  

    # Iterate through each character as potential center
    for i in range(len(s)):
        # Case 1: Odd-length palindrome (single center)
        odd_pal = expand_from_center(i, i)
        # Case 2: Even-length palindrome (center between two chars)
        even_pal = expand_from_center(i, i + 1)

        # Choose the longer 
        current_longest = odd_pal if len(odd_pal) > len(even_pal) else even_pal

        # Update result if current palindrome is longer
        if len(current_longest) > len(longest):
            longest = current_longest

    return longest



# print(longestPalindrome("babad"))  # Output: "bab" or "aba"
# print(longestPalindrome("cbbd"))   # Output: "bb"
# print(longestPalindrome("a"))      # Output: "a"
# print(longestPalindrome("ac"))     # Output: "a" or "c"
