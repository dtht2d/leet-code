"""
Problem: Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such
that each unique element appears only once. The relative order of the elements should be kept the same.
Return: the number of unique k elements in nums
Consider the number of unique elements of nums to be k, to get accepted, need to do the following things:
        -   Change the array nums such that the first k elements of nums contain the unique elements in the order
        they were present in nums initially.
        -   The remaining elements of nums are not important as well as the size of nums.
Constraints:
        -   0 <= nums.length <= 3 * 10^4
        -   -100 <= nums[i] <= 100
        -   nums is sorted in non-decreasing order.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        # Condition 1: 0 <= nums.length <= 3 * 10^4
        c1 = (0 <= len(nums) <= 3 * (10 ** 4))
        # Condition 2: -100 <= nums[i] <= 100 for all elements in nums
        c2 = all(-100 <= num <= 100 for num in nums)
        # Condition 3: nums is sorted in non-decreasing order
        c3 = all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1))
        if c1 and c2 and c3:
            k = 1
            for i in range(1, len(nums)):
                if nums[i] != nums[i - 1]:
                    nums[k] = nums[i]
                    k += 1
            return k, nums[:k]
        else:
            raise ValueError("Invalid input")
#Example
nums= [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
s = Solution()
k, nums_unique = s.removeDuplicates(nums)
print(k, nums_unique)