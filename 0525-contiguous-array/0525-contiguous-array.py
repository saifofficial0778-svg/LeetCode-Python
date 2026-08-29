class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        max_len=float('-inf')
        for i in range(n):
            if nums[i]==0:
                nums[i]=-1

        mydict={0:-1}
        curr_sum=0
        for i in range(n):
            curr_sum+=nums[i]

            if curr_sum in mydict:
                max_len=max(max_len,i-mydict[curr_sum])
            else:
                mydict[curr_sum]=i
        if max_len==float('-inf'):
            return 0
        return max_len