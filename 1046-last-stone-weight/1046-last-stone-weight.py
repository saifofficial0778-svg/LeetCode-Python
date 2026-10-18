import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap=[]
        for stone in stones:
            heapq.heappush(heap,-stone)

        while len(heap)>1:
            y=-heapq.heappop(heap)
            x=-heapq.heappop(heap)

            if x==y:
                continue
            else:
                heapq.heappush(heap,-(y-x))
        if heap:
            return -heapq.heappop(heap)
        else:
            return 0
        