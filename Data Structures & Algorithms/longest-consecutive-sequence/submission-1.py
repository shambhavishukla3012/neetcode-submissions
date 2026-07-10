class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # longest = 0
        
        # for n in nums:
        #     count = 1
        #     while n-1 in nums:
        #         count+=1
        #         n = n-1
        #     longest =max(longest, count)

        # return longest


        longest = 0

        numSet = set(nums)

        for num in numSet:
            if (num-1) not in numSet:
                length = 1
                while (num+length) in numSet:
                    length +=1
                longest = max(longest, length)
        return longest
