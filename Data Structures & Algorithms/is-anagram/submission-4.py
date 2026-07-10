class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashMap = {}

        for i in s:
            if i in hashMap:
                hashMap[i]+=1
            else:
                hashMap[i]=1

        for j in t:
            if j not in hashMap:
                return False
            hashMap[j]-=1

        for val in hashMap.values():
            if val != 0:
                return False
        return True



        
