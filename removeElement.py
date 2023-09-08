class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new = []
        for i in range(len(nums)):
            if nums[i] != val:
                new.append(nums[i])
        nums[:] =  new
        return len(nums)
