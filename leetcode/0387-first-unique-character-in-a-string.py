# Count every character in a hash map, then scan the string again and
# return the index of the first character whose count is 1 (or -1).
# Time: O(n), Space: O(1)   (at most 26 keys for lowercase Latin letters)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        for i, ch in enumerate(s):
            if freq[ch] == 1:
                return i
        return -1
