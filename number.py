class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        most_water=0
        while left<=right:
            water=(right-left)*min(height[left],height[right])
            most_water=max(water,most_water)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return most_water