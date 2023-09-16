class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area = 0
        while left<right:
            h = min(height[left],height[right])
            w = right - left
            area = max(area,h*w)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return area
        # area = 0
        # for i in range(len(height)):
        #     for j in range(i,len(height)):
        #         area = max(area,((j-i) * min(height[i], height [j])))
        # return area
