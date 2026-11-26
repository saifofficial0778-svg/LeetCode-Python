import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        mydict={}
        heap=[]
        for task in tasks:
            mydict[task]=mydict.get(task,0)+1

        for count in mydict.values():
            heapq.heappush(heap,(-count))

        d=deque()
        time=0

        while heap or d:
            time+=1

            while d and d[0][1]<=time:
                count,relesed_time=d.popleft()
                heapq.heappush(heap, count)

            if heap:
                count=heapq.heappop(heap)
                count+=1

                if count<0:
                    d.append((count,time+n+1))
        return time
                




        
        