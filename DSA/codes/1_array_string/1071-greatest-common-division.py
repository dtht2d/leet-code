"""
1071. Greatest Common Divisor of Strings
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t
(i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2.
Return the largest string x such that x divides both str1 and str2.
Constraint:
    1 <= str1.length, str2.length <= 1000
    str1 and str2 consist of English uppercase letters.
"""
import math
class Solution:
    def gcdOfStrings(self, s: str, t: str) -> str:
        if not (len(s) >= 1 or len(t) <= 1000 or s.isalpha() or t.isalpha() or s.isupper() or t.isupper()):
            raise ValueError("Invalid input")
        # s =  t+..t or therefore s = nt and s+t should be equal to s+t if t is concatenated with itself n times
        if s + t != t + s:
                return ""
        gcd = math.gcd(len(s), len(t))
        return s[:gcd]
#Example
s="ABABAB"
t="ABAB"
result = Solution().gcdOfStrings(s,t)
print (result)