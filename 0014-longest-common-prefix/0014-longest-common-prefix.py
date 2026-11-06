class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        strs.sort()

        first = strs[0]
        last = strs[-1]

        for i, char in enumerate(first):
            if i >= len(last) or char != last[i]:
                return first[:i]

        return first
        