nums =[1,2,3,5,7,7,8,8,9,9,9,]
nums = [x for i, x in enumerate(nums) if nums.index(x) != i]
print(nums)