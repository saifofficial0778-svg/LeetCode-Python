import heapq
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        mydict={}
        for ch in words:
            mydict[ch]=mydict.get(ch,0)+1

        heap=[]

        for num,freq in mydict.items():
            heapq.heappush(heap,(-freq,num))

        ans=[]

        for _ in range(k):
            freq,num=heapq.heappop(heap)
            ans.append(num)
        return ans