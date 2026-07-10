class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = defaultdict(int)
        for n in nums:
            hashMap[n] += 1

        
        for k,v in hashMap.items():
            if v > len(nums)//2 :
                return k 
