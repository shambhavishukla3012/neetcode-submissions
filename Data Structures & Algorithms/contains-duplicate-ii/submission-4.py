class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # hashMap ={}

        # for i, n in enumerate(nums):
        #     if n in hashMap and i - hashMap[n] <= k:
        #         return True
        #     hashMap[n] = i

        # return False


        window = set()
        L = 0

        for R in range(len(nums)):
            if R-L>k:
                window.remove(nums[L])
                L+=1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False