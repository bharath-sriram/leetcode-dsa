class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        take = 10
        alice_turn = True
        while n >= take:
            n -= take
            take -= 1
            alice_turn = not alice_turn
        return not alice_turn