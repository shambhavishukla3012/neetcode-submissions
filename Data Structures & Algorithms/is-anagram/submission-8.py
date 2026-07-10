class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashMap = {}
        for a in s:
            if a in hashMap:
                hashMap[a] += 1 
            else:
                hashMap[a] = 1

        for b in t:
            if b not in hashMap:
                return False
            else:
                hashMap[b]-=1
        
        for val in hashMap.values():
            if val != 0:
                return False
        return True

