"""
Problem: Given a string s, reverses only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o' and 'u' and they can appear in both upper and lower cases more than once.
Example 1:
    Input: s = "hello"
    Output: "holle"
Example 2:
    Input: s = "leetcode" -> vowels in s[1]='e', s[2]='e', s[5]='o', s[7]='e'
    reverse vowels order appearance    s[7]='e', s[5]='e', s[2]='e', s[1]='e'
    Output: "leotcede"
Constraints:
    1 <= s.length <= 3*10^5
    s consist of printable ASCII characters
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        #Vowels list only have unique characters
        vowels = set("aeiuoAEIUO")
        #Change string to list so it can be easier to manipulate
        #since each element has  its corresponding index
        s_list = list(s)
        vowels_position = []
        for i,char in enumerate(s_list):
            #Get vowels character and its index
            if char in vowels:
                vowels_position.append((i,char))
        #Access character in each pair of reversed vowels position list
        reversed_vowels_char = [vowel[1] for vowel in vowels_position[::-1]]
        #Get original vowels index
        vowels_index = [vowel[0] for vowel in vowels_position]
        for i, char in enumerate(s_list):
            if char in vowels:
                s_list[i] = reversed_vowels_char[vowels_index.index(i)]
        return ''.join(s_list)
#Test line by line
#Make sure the vowels list can't contain duplicate elements
vowels = set("aeiouAEIOU")
s = "leetcode"
s_list = list(s)
vowels_pos = []
#Find index of vowels in s
#Iterate over each element in s_list along with its index to get vowel character at its index
for i,char in enumerate(s_list):
    if char in vowels:
        vowels_pos.append((i,char))
        print("Vowels index in original s_list", i,char)
#Get reverse vowels character list
reversed_vowels_list = [vowel[1] for vowel in vowels_pos[::-1]]
#Get the original index
vowels_index_og = [vowel[0] for vowel in vowels_pos]
result = []
for i, char in enumerate(s_list):
    if char in vowels:
        s_list[i] = reversed_vowels_list[vowels_index_og.index(i)]
        #No space betwwen character ''
        result = "".join(s_list)
print(result)

#Example for class function
s = "Courtney"
result = Solution().reverseVowels(s)
print(type(result))