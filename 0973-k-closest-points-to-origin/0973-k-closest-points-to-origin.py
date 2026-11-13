import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap=[]
        for point in points:
            d=point[0]**2+point[1]**2
            heapq.heappush(heap,(d,point))
        ans=[]
        for _ in range(k):
            d,point=heapq.heappop(heap)
            ans.append(point)
        return ans
        