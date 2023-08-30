"""
This function merge two strings by adding letters in alternating order.
If a string is longer than the other, append the additional letters
onto the end of the merged string.
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge = " "
        len1, len2 = len(word1), len(word2)
        min_range = min(len1,len2)
        for i in range(min_range):
            merge += word1[i] +word2[i]
        #Add remain letters from longer word
        if len1 > len2:
            merge += word1[min_range:]
        else:
            merge += word2[min_range:]
        return merge
#Example
s = Solution()
word1 = "Joy"
word2 = "Life"
merge = s.mergeAlternately(word1,word2)
print (merge)
