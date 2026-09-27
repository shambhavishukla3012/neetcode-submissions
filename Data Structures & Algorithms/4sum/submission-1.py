# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         nums.sort()
#         n = len(nums)
#         res = []

#         for i in range(n):
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             for j in range(i + 1, n):
#                 if j > i + 1 and nums[j] == nums[j - 1]:
#                     continue
#                 left, right = j + 1, n - 1
#                 while left < right:
#                     total = nums[i] + nums[j] + nums[left] + nums[right]
#                     if total == target:
#                         res.append([nums[i], nums[j], nums[left], nums[right]])
#                         left += 1
#                         right -= 1
#                         while left < right and nums[left] == nums[left - 1]:
#                             left += 1
#                         while left < right and nums[right] == nums[right + 1]:
#                             right -= 1
#                     elif total < target:
#                         left += 1
#                     else:
#                         right -= 1

#         return res



class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, quad = [], []

        def kSum(k, start, target):
            if k == 2:
                l, r = start, len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] < target:
                        l += 1
                    elif nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        res.append(quad + [nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                return

            for i in range(start, len(nums) - k + 1):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                quad.append(nums[i])
                kSum(k - 1, i + 1, target - nums[i])
                quad.pop()

        kSum(4, 0, target)
        return res