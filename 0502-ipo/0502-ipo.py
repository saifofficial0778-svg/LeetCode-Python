import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        projects=list(zip(capital,profits))
        projects.sort()

        i=0
        heap=[]

        for _ in range(k):
            while i<len(projects) and projects[i][0]<=w:
                heapq.heappush(heap,-projects[i][1])    
                i+=1    

            if not heap:
                break
            w+=-heapq.heappop(heap)
        return w