import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq={}
        for task in tasks:
            freq[task]=freq.get(task,0)+1
       
        heap=[-count for count in freq.values() ]
        heapq.heapify(heap)

        d=deque()
        time=0

        while heap or d:
            time+=1

            if d and d[0][1]<=time:
                count,relase_time=d.popleft()
                heapq.heappush(heap,count)

            if heap:
                count=heapq.heappop(heap)

                count+=1

                if count<0:
                    d.append((count,time+n+1))
        return time

        