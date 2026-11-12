import heapq
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        mydict={}
        for ch in words:
            mydict[ch]=mydict.get(ch,0)+1

        heap=[]

        for ch , freq in mydict.items():
            heapq.heappush(heap,(-freq,ch))
        ans=[]
        for _ in range(k):
            freq, ch=heapq.heappop(heap)
            ans.append(ch)

        return ans

        