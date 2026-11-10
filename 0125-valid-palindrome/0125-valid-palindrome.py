class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new = "".join(char.lower() for char in s if char.isalnum())

        return new == new[::-1]