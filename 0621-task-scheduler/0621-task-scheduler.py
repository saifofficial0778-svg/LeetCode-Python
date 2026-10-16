import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1

        heap = [-count for count in freq.values()]
        heapq.heapify(heap)

        q = deque()
        time = 0

        while heap or q:
            time += 1

            if q and q[0][1] <= time:
                count, release_time = q.popleft()
                heapq.heappush(heap, count)

            if heap:
                count = heapq.heappop(heap)
                count += 1

                if count < 0:
                    q.append((count, time + n + 1))

        return time