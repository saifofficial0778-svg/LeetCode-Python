import heapq
from collections import deque
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1

        heap=[(-count ,ch) for ch,count in freq.items()]
        heapq.heapify(heap)

        d=deque()
        time=0
        ans=""

        while heap or d:
            time+=1

            if d and d[0][2]<=time:
                count,ch,release_time=d.popleft()
                heapq.heappush(heap,(count,ch))

            if heap:
                count,ch=heapq.heappop(heap)
                ans+=ch

                count+=1

                if count<0:
                    d.append((count,ch,time+2))
            elif d:
                return ""
        return ans



        

        