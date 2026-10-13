import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap=[]
        for point in points:
            sqrt=point[0]**2+point[1]**2
            heapq.heappush(heap,(sqrt,point))
        ans=[]
        for _ in range(k):
            sqrt ,point=heapq.heappop(heap)
            ans.append(point)
        return ans
