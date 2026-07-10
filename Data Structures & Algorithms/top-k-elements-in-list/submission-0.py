class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}

        for n in nums:
            if n in hashMap:
                hashMap[n] += 1
            else:
                hashMap[n] = 1
        
        freq = [[] for i in range(len(nums) + 1)]

        for v, i in hashMap.items():
            freq[i].append(v)
            print(freq)

        print(freq)    
        
        res =[]
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res