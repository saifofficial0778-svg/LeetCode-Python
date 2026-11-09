import heapq
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        heap=[]
        fuel=startFuel
        stops=0

        for pos , gas in stations:
            while fuel<pos:
                if not heap:
                    return -1
                fuel+=-heapq.heappop(heap)
                stops+=1
            heapq.heappush(heap,-gas)

        while target>fuel:
            if not heap :
                return -1
            fuel+=-heapq.heappop(heap)
            stops+=1
        return stops
        