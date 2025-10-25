# -------------------------------------------------------------
# LeetCode Problem 165: Compare Version Numbers
# -------------------------------------------------------------
# Description:
# Given two version numbers, version1 and version2, compare them.
#
# A version number consists of one or more revisions joined by a dot '.'.
# Each revision consists of digits and may contain leading zeros.
# Each revision is compared as an integer.
#
# Return:
#   - 1  if version1 > version2
#   - -1 if version1 < version2
#   - 0  if they are equal
#
# -------------------------------------------------------------
# Examples:
# Example 1:
#   Input:  version1 = "1.01", version2 = "1.001"
#   Output: 0
#   Explanation: Leading zeros are ignored ("01" = "1").
#
# Example 2:
#   Input:  version1 = "1.0", version2 = "1.0.0"
#   Output: 0
#
# Example 3:
#   Input:  version1 = "0.1", version2 = "1.1"
#   Output: -1
#
# Example 4:
#   Input:  version1 = "1.0.1", version2 = "1"
#   Output: 1
#
# Example 5:
#   Input:  version1 = "7.5.2.4", version2 = "7.5.3"
#   Output: -1
#
# -------------------------------------------------------------
# Constraints:
#   - 1 <= version1.length, version2.length <= 500
#   - version1 and version2 consist only of digits and '.'
#   - version1 and version2 are valid version numbers
#   - No leading or trailing dots
# -------------------------------------------------------------
# Approach Used: String Parsing + Two Pointers
# -------------------------------------------------------------
# Idea:
# - Split each version string by '.' into integer lists.
# - Compare corresponding parts one by one.
# - If one list is shorter, treat missing parts as 0.
#
# Time Complexity:  O(n)
# Space Complexity: O(n) or O(1) (if parsed on-the-fly)
# -------------------------------------------------------------


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split versions by '.'
        v1 = version1.split('.')
        v2 = version2.split('.')

        # Determine max length to compare all levels
        n = max(len(v1), len(v2))

        # Compare each revision
        for i in range(n):
            # Convert to int to remove leading zeros
            num1 = int(v1[i]) if i < len(v1) else 0
            num2 = int(v2[i]) if i < len(v2) else 0

            # Compare corresponding revisions
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1

        # If all revisions equal
        return 0

sol = Solution()

# -------------------------------------------------------------
# Example Runs (uncomment to test)
# -------------------------------------------------------------
# print(sol.compareVersion("1.01", "1.001"))   # Output: 0
# print(sol.compareVersion("1.0", "1.0.0"))    # Output: 0
# print(sol.compareVersion("0.1", "1.1"))      # Output: -1
# print(sol.compareVersion("1.0.1", "1"))      # Output: 1
# print(sol.compareVersion("7.5.2.4", "7.5.3"))# Output: -1
