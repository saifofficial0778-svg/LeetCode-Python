import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap=[]
        for num in nums:
            heapq.heappush(heap,-num)

        for _ in range(k):
            num=-heapq.heappop(heap)

        return num

        



        