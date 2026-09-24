class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        lkp = {}
        for a in s:
            if a not in lkp:
                lkp[a] = 1
            else:
                lkp[a] += 1

        for b in t:
            if b not in lkp:
                return False
            lkp[b] -=1
        

        for val in lkp.values():
            if val != 0:
                return False
        return True
