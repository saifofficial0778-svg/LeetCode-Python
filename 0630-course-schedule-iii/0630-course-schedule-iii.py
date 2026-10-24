import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        heap=[]
        total=0

        for duration , last_day in courses:
            total+=duration
            heapq.heappush(heap,-duration) 

            if total>last_day:
                longest=-heapq.heappop(heap)
                total-=longest      
        return len(heap)