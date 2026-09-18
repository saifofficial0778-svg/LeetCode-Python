class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        n,m=len(firstList),len(secondList)
        i,j=0,0
        res=[]
        while i<n and j<m:
            start=max(firstList[i][0],secondList[j][0])
            end=min(firstList[i][1],secondList[j][1])
            if start<=end:
                res.append([start,end])

            if firstList[i][1]<=secondList[j][1]:
                i+=1
            else:
                j+=1
        return res
