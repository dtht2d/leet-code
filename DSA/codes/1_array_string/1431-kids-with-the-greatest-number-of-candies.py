"""
1431. Kids With the Greatest Number of Candies
Problem: There are n kids with candies. You are given an integer array candies, where each candies[i] represents
the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies,
they will have the greatest number of candies among all the kids, or false otherwise.
Note that multiple kids can have the greatest number of candies.
"""
import numpy as np
from typing import List
class Solution:
    def kidsWithCandies(selfself, candies: List[int], extraCandies: int ) -> List [bool]:
        max_candy = max(candies)
        result = [ i + extraCandies >= max_candy for i in candies]
        return result

#Example
candies = [2,3,5,1,3]
extraCandies = 3
s = Solution().kidsWithCandies(candies,extraCandies)
print (s)