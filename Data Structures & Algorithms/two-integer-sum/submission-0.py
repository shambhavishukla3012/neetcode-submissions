class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, n in enumerate(nums):
            d = target - n
            if d in hashMap:
                return [hashMap[d], i]
            hashMap[n] = i 