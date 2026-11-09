class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        running_sum = [nums[0]]
        for i in range(1, len(nums)):
            running_sum.append(nums[i] + running_sum[i-1])
        
        return running_sum