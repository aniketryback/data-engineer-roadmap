#BIT MANIPULATION
class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        count = 0

        xor = start ^ goal

        while (xor > 0):
            if (xor & 1) == 1:
                count += 1
            xor >>= 1
        return count
