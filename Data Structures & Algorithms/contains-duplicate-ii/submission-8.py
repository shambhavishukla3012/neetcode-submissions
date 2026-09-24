class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lkp = {}

        for i, n in enumerate(nums):
            if n in lkp and i - lkp[n] <= k:
                return True
            lkp[n] = i
        return False