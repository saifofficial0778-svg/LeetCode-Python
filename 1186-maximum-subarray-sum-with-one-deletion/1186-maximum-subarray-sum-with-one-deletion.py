class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        delete=float('-inf')
        res=arr[0]
        keep=arr[0]
        curr_sum=0

        for i in range(1,len(arr)):
            curr_sum=arr[i]

            old_dlt=delete
            old_keep=keep

            keep=max(old_keep+arr[i],arr[i])
            delete=max(old_dlt+arr[i],old_keep)
            res=max(res,keep,delete)
        return res


        