class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        hashMap = {0:1}
        count = 0
        curSum = 0

        for n in nums:
            curSum+=n
            diff = curSum-k

            if diff in hashMap:
                count += hashMap[diff]

            if curSum in hashMap:
                hashMap[curSum] += 1
            else:
                hashMap[curSum] = 1

        return count