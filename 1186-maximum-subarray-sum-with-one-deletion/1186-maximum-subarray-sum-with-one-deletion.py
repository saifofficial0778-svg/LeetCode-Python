class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        delete=float('-inf')
        n=len(arr)
        keep=arr[0]
        ans=arr[0]
        for i in range(1,n):
            curr=arr[i]

            old_keep=keep
            old_delete=delete
            
            keep=max(old_keep+curr,curr)
            delete=max(old_delete+curr,old_keep)

            ans=max(ans,keep,delete)
        return ans
