class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # prefix = ""

        # for i in range(len(strs[0])):
        #     for s in strs[1:]:
        #         if i == len(s) or s[i] != strs[0][i]:
        #             return prefix
        #     prefix += strs[0][i]
        # return prefix
        
        for i in range(len(strs[0])):
            for s in strs[1:]:
                if i == len(s) or s[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]



            