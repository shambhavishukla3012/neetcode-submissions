class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        op= []
        i = 0
        n, m =len(word1), len(word2)

        for i in range(max(n,m)):
            if i<n:
                op.append(word1[i])
            if i<m:
                op.append(word2[i])
        return"".join(op)