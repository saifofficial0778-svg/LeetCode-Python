import heapq
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        heap=[]
        fuel=startFuel
        stop=0

        for pos , gas in stations:
            while fuel<pos:
                if not heap:
                    return -1
                fuel+=-heapq.heappop(heap)
                stop+=1
            heapq.heappush(heap,-gas)

        while fuel<target:
            if not heap:
                return -1
            fuel+=-heapq.heappop(heap)
            stop+=1
        return stop

                
        