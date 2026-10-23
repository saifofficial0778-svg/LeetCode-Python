import heapq
class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        heap=[]
        for i, row in enumerate(mat):
            count=0
            for col in row:
                if col==1:
                    count+=1
            heapq.heappush(heap,(count,i))
        ans=[]
        for _ in range(k):
            count,row=heapq.heappop(heap)
            ans.append(row)
        return ans
                
        