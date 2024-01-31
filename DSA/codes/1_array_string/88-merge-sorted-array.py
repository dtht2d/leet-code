"""
Problem: Given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be sorted inside the array nums1.
To accommodate this, nums1 has a length of m+n, where the first m element denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n
Example:
     Input nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
     Output: A=[1,2,2,3,5,6]
     Explanation:
        The arrays we are merging are [1,2,3] and [2,5,6].
        The result of the merge is [1,2,2,3,5,6] with [A][0,1,3] are elements coming from nums1.
Constraints:
nums.length == m+n
nums2.length == n
0<=m, n<=200
-10^9 <= nums1[i], nums2[i] <= 10^9
"""
class Solution:
    def merge(self , nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1[:] = sorted(nums1[:m] + nums2)
        return nums1
#Test
#Example 1
nums1 = [1,2,3,0,0,0]
m, n = 3, 2
nums2 = [2,5,6]
s_ex1 = Solution().merge(nums1,m,nums2,n)
print(s_ex1)

#Example 2
nums1 = [1]
m, n = 1, 0
nums2 = []
s_ex2 = Solution().merge(nums1,m,nums2,n)
print(s_ex2)

#Example 3
nums1 = [0]
m, n = 0, 1
nums2 = [1]
s_ex3 = Solution().merge(nums1,m,nums2,n)
print(s_ex3)
