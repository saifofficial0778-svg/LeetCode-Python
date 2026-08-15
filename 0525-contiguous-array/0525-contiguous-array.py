class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        mydict={0:-1}
        for i in range(n):
            if nums[i]==0:
                nums[i]=-1
            else:
                nums[i]=1
        prefix_sum=0
        max_len=0
        for i in range(n):
            prefix_sum+=nums[i]

            if prefix_sum in mydict:
                max_len=max(max_len,i-mydict[prefix_sum])
            else:
                mydict[prefix_sum]=i
        return max_len