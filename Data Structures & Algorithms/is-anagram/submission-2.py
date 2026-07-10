class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        hashMap = {}

        for i in range(len(s)):
            if s[i] in hashMap:
                hashMap[s[i]] += 1
            else:
                hashMap[s[i]] = 1

        for i in range(len(t)):
            if t[i] in hashMap:
                hashMap[t[i]] -= 1
            else:
                return False

        for index in hashMap.values():
            if index != 0:
                return False
        return True        

            