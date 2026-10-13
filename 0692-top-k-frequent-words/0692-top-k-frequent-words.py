import heapq
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        mydict={}

        for ch in words:
            mydict[ch]=mydict.get(ch,0)+1

        heap=[]

        for word , freq in mydict.items():
            heapq.heappush(heap,(-freq,word))

        ans=[]
        for _ in range(k):
            freq , word = heapq.heappop(heap)
            ans.append(word)
        return ans