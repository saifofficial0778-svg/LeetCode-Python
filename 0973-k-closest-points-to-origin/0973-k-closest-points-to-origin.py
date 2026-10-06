import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap=[]
        ans=[]
        for point in points:
            d=point[0]**2+point[1]**2
            heapq.heappush(heap,(-d,point))

            if len(heap)>k:
                heapq.heappop(heap)
                
        for d,p in heap:
            ans.append(p)
        return ans

        

        
        