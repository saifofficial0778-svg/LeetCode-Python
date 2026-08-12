class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        delete=float('-inf')
        keep=arr[0]
        ans=arr[0]

        for i in range(1,len(arr)):
            curr=arr[i]

            old_keep=keep
            old_delete=delete

            keep=max(old_keep+curr,curr)
            delete=max(old_delete+curr,old_keep)

            ans=max(keep,ans,delete)
        return ans
