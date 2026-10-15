import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap=[]
        for num in arr:
            d=abs(x-num)
            heapq.heappush(heap,(-d,-num))

            if len(heap)>k:
                heapq.heappop(heap)
        ans=[]
        for d, num in heap:
            ans.append(-num)
        ans.sort()
        return ans
