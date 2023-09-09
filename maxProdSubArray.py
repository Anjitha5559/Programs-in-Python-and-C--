class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev_min = prev_max = global_max = nums[0]
        for num in nums[1:]:
            cur_min = min(prev_min*num,prev_max*num,num)
            cur_max = max(prev_min*num,prev_max*num,num)
            global_max = max(cur_max,global_max)
            prev_min = cur_min
            prev_max = cur_max
        return global_max