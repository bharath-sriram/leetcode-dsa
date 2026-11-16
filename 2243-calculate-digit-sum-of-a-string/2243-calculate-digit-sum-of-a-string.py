class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while len(s) > k:
            new_s = []
            for i in range(0, len(s), k):
                chunk = s[i:i+k]
                new_s.append(str(sum(int(d) for d in chunk)))
            s = "".join(new_s)
        return s