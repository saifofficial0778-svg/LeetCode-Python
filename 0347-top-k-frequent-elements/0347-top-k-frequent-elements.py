import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1

        heap=[(-count,num) for num,count in freq.items()]
        heapq.heapify(heap)

        ans=[]

        for _ in range(k):
            count,num=heapq.heappop(heap)

            ans.append(num)
        return ans

