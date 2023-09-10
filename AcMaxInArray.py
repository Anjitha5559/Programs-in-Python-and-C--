nums = [1,2,3,4,5,2]
max_ele = nums[0]
for i in range(1,len(nums)):#0 t0 5
    if nums[i] > max_ele:#
        max_ele = max(max_ele,nums[i])
print(max_ele)
print(nums.index(max_ele))

        

    
    