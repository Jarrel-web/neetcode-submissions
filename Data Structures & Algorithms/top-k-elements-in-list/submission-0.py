class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        numCount = {}
        for num in nums:
                numCount[num] = 1 + numCount.get(num, 0)
        arr = []
        for num, count in numCount.items():
            arr.append([count,num])
        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res