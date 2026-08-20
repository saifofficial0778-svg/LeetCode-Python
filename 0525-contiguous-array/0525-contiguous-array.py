class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        mydict={0:-1}
        max_len=0
        for i in range(0,n):
            if nums[i]==0:
                nums[i]=-1
            else:
                nums[i]=1
        curr_sum=0
        for i in range(0,n):
            curr_sum+=nums[i]

            if curr_sum in mydict:
                max_len=max(max_len,i-mydict[curr_sum])
            else:
                mydict[curr_sum]=i
        return max_len




        

            
        
        