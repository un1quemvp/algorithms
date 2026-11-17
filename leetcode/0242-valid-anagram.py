# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         dict_of_words ={}
#         if len(s) != len(j):
#             return False
#         for i in s:
#             dict_of_words[i] = 1
#         for j in t:
#             if j in dict_of_words:
#                 del d[j]
#         if len(dict_of_words) == 0:
#             return True
##более быстрое решение, исп. меньше память
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts ={}
        if len(s) != len(t):
            return False
        for c in s:
            counts[c] = counts.get(c, 0) + 1
        for c in t:
            if c in counts:
                counts[c]-=1   
        return all(value == 0 for value in counts.values())