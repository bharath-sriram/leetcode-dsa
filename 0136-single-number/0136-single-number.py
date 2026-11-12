class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        for key, value in count.items():
            if value == 1:
                return key