class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # hashMap = defaultdict(int)
        # for n in nums:
        #     hashMap[n] += 1
        
        # for k,v in hashMap.items():
        #     if v > len(nums)//2 :
        #         return k 

        res = 0
        count = 0

        for n in nums:
            if count == 0:
                res = n
            if n == res:
                count+=1
            else:
                count -=1
        return res