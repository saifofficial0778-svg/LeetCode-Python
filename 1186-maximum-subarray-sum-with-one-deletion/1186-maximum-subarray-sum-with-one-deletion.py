class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        delete=float('-inf')
        res=arr[0]
        keep=arr[0]
        curr_sum=0
        for i in range(1,len(arr)):
            curr_sum=arr[i]

            old_keep=keep
            old_dlt=delete

            keep=max(old_keep+curr_sum,curr_sum)
            delete=max(delete+curr_sum,old_keep)

            res=max(res,keep,delete)
        return res
        