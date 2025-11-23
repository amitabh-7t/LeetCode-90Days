class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

#####

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


#####

from collections import Counter
s = "anagram"
count = Counter(s)
print(count)

{'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
