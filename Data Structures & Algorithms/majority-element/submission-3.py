class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count = {}
        # for n in nums:
        #     if n in count:
        #         count[n]+=1
        #     else:
        #         count[n] = 1

        # for k,v in count.items():
        #     if v>len(nums)//2:
        #         return k
        # count = {}
        # res, maxCount = 0, 0
        # for n in nums:
        #     if n in count:
        #         count[n]+=1
        #         res = n if count[n]>maxCount else res
        #         maxCount = max(count[n], maxCount)
        #     else:
        #         count[n] = 1
        # return res

     
        count, res = 0, 0

        for n in nums:
            if count == 0:
                res = n
            count += 1 if n == res else -1

        return res



        
