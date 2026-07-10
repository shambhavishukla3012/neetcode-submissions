class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False

        hashMap ={}

        for a in s:
            if a not in hashMap:
                hashMap[a]=1
            else:
                hashMap[a]+=1
        
        for a in t:
            if a in hashMap:
                hashMap[a]-=1
            else:
                return False

        for a in hashMap.values():
            if a != 0:
                return False
        return True
        