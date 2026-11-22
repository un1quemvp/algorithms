# Sum the values of all symbols, then subtract twice the value of every symbol
# that stands before a larger one (subtractive pairs like IV, IX).
# Time: O(n), Space: O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        dict_word = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        total = 0
        counter = 0
        for i in s:
            total += dict_word[i]
        for i in range(1, len(s)):
            if dict_word[s[i-1]] < dict_word[s[i]]:
                counter += dict_word[s[i-1]]
        return total - counter*2
