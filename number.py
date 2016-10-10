class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x == 1 or x == 2 or x == 3:
            return 1
        i = 2
        while i ** 4 < x:
            i = i ** 2
        left = i
        right = i ** 2
        while right - left > 1:
            mid = (left + right) / 2
            t = mid ** 2
            if t == x:
                return mid
            if t < x:
                left = mid
            else:
                right = mid
        return left
