import heapq
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        fuel=startFuel
        stop=0
        heap=[]

        for pos,gas in stations:
            while fuel<pos:
                if not heap:
                    return -1
                fuel+=-heapq.heappop(heap)
                stop+=1
            heapq.heappush(heap,-gas)

        while target>fuel:
            if not heap:
                return -1
            fuel+=-heapq.heappop(heap)
            stop+=1
        return stop

        