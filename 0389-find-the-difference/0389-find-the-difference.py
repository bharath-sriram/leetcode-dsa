class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        diff = sum(ord(c) for c in t) - sum(ord(c) for c in s)
        return chr(diff)