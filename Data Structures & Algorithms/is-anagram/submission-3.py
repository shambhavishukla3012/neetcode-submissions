class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # hashMap = {}

        # for a in s:
        #     if a not in hashMap:
        #         hashMap[a] = 1
        #     else:
        #         hashMap[a] +=1
        
        # for b in t:
        #     if b not in hashMap:
        #         return False
        #     else:
        #         hashMap[b] -=1

        # for v in hashMap.values():
        #     if v!=0:
        #         return False
        # return True
            

        count =[0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] +=1
            count[ord(t[i])- ord('a')] -=1

        for c in count:
            if c != 0:
                return False
        return True
