class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lkp = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in lkp:
                return [ lkp[diff], i ]
            lkp[n] = i
        
    