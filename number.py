class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result=0
        left=0
        right=len(height)-1
        water_level=0

        while left<=right:
            if height[left]<=height[right]:
                if height[left]<=water_level:
                    result+=(water_level-height[left])
                else:
                    water_level=height[left]
                left+=1
            else:
                if height[right]<=water_level:
                    result+=(water_level-height[right])
                else:
                    water_level=height[right]
                right-=1
        return result