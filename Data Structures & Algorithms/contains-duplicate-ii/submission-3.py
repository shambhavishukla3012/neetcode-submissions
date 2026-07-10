class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap ={}

        for i, n in enumerate(nums):
            if n in hashMap and i - hashMap[n] <= k:
                return True
            hashMap[n] = i

        return False