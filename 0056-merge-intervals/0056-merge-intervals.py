class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        res=[]
        start=intervals[0][0]
        end=intervals[0][1]

        for i in range(1,len(intervals)):
            start1=intervals[i][0]
            end1=intervals[i][1]

            if start1<=end:
                end=max(end,end1)
            else:
                res.append([start,end])
                start=start1
                end=end1
        res.append([start,end])
        return res
            