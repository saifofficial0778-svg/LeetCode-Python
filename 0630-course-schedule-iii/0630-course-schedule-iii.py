import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])

        total=0
        heap=[]

        for duration , lastDay in courses:
            total+=duration
            heapq.heappush(heap,-duration)

            if total>lastDay:
                longest=-heapq.heappop(heap)
                total-=longest
        return len(heap)