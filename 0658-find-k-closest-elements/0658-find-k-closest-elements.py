import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap=[]
        for num in arr:
            heapq.heappush(heap,(-abs(x-num),-num))

            if len(heap)>k:
                heapq.heappop(heap)
        ans=[]
        for dis,num in heap:
            ans.append(-num)
        ans.sort()
        return ans

