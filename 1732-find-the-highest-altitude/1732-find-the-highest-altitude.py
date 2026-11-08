class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        highest = [0]
        for i in range(len(gain)):
            highest.append(highest[i] + gain[i])

        return max(highest)