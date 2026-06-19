class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        max_area=0

        while left<right:
            #calculate
            width=right-left
            left_height=height[left]
            right_height=height[right]
            current_area=width*min(left_height,right_height)
            max_area=max(max_area, current_area)
            if left_height < right_height:
                left += 1
            else:
                right -= 1
        return max_area