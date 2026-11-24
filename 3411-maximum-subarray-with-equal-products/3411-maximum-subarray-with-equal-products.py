class Solution(object):
    def maxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(nums)
        ans = 1
        for i in range(n):
            prod = nums[i]
            g = nums[i]
            l = nums[i]
            for j in range(i + 1, n):
                prod *= nums[j]
                g = gcd(g, nums[j])
                l = (l * nums[j]) // gcd(l, nums[j])
                if prod == l * g:
                    ans = max(ans, j - i + 1)
        return ans