class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while low<=high:
            if nums[low]<=nums[high]:
                return nums[low]
            mid = (low+high)//2
            if nums[low]>nums[mid]:
                high = mid
            else:
                low = mid + 1
                
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]