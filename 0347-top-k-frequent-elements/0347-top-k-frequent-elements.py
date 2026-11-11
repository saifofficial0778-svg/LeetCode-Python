import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        mydict={}
        for num in nums:
            mydict[num]=mydict.get(num,0)+1

        heap=[]

        for ch , freq in mydict.items():
            heapq.heappush(heap,(-freq,ch))
        res=[]
        for _ in range(k):
            freq,ch=heapq.heappop(heap)
            res.append(ch)

        return res
        