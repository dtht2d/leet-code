"""
Problem: You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
and an integer n, return true if n new flowers can be planted in the flowerbed without violating the
no-adjacent-flowers rule and false otherwise.
Constraints:
    1 <= flowerbed.length <= 2 * 104
    flowerbed[i] is 0 or 1.
    There are no two adjacent flowers in flowerbed.
    0 <= n <= flowerbed.length
"""

from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        flowerbed = [0] + flowerbed + [0]  # Adding 0's at the beginning and end to handle edge cases
        i = 1
        while i < len(flowerbed) - 1:
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                count += 1
            i += 1
        return count >= n

#Example
flowerbed = [0,0,1,1,1,0,0,1,0,0]
s = Solution()
result_1 = s.canPlaceFlower(flowerbed, n=1)
result_2 = s.canPlaceFlower(flowerbed, n=3)
print("result_1", result_1)
print("result_2", result_2)
