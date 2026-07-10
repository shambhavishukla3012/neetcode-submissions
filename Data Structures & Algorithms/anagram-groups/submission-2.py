class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        op = defaultdict(list)
        
        for s in strs:
            
            count =[0] * 26
            
            for a in s:
                count[ord(a) - ord('a')]+=1
            op[tuple(count)].append(s)

        return list(op.values())