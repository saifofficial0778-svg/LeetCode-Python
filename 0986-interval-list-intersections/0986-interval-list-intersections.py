class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n=len(firstList)
        m=len(secondList)
        res=[]
        i = 0
        j = 0

        while i < n and j < m:
            start1=firstList[i][0]
            end1=firstList[i][1]

            start2=secondList[j][0]
            end2=secondList[j][1]

            start=max(start1,start2)
            end=min(end1,end2)

            if start<=end:
                res.append([start,end])
            if firstList[i][1]<secondList[j][1]:
                i+=1
            else:
                j+=1
        return res