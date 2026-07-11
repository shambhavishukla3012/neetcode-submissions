class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPalin(i,j):
            while i<j:     
                if s[i] != s[j]:
                    return False                    
                i+=1
                j-=1
            return True

        i, j = 0, len(s)-1
        while i <j:
            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                return isPalin(i+1,j) or isPalin(i,j-1)
        return True