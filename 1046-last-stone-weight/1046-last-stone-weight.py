import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap=[]
        for stone in stones:
            heapq.heappush(heap,-stone)
        
        while len(heap)>=2:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if x==y:
                continue
            else:
                heapq.heappush(heap,-(x-y))
        if heap:
            return -heapq.heappop(heap)
        else:
            return 0