class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i,n in enumerate(nums):
            diff = target - n

            if diff not in hashMap:
                hashMap[n] = i
            else:
                return [hashMap[diff], i]
        return False
