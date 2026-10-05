import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        mydict = {}

        for num in nums:
            mydict[num] = mydict.get(num, 0) + 1

        heap = []

        for num, freq in mydict.items():
            heapq.heappush(heap, (-freq, num))

        ans = []

        for _ in range(k):
            freq, num = heapq.heappop(heap)
            ans.append(num)

        return ans