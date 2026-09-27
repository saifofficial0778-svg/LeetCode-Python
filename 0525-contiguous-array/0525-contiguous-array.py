class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mydict={0:-1}
        max_len=0
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i]=-1
        prefix_sum=0
        for i in range(len(nums)):
            prefix_sum+=nums[i]

            if prefix_sum in mydict:
                max_len=max(max_len,i-mydict[prefix_sum])
            else:
                mydict[prefix_sum]=i
            
        return max_len



