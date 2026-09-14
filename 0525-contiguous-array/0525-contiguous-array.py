class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mydict={0:-1}
        max_len=0
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i]=-1

        curr_sum=0
        for i in range(len(nums)):
            curr_sum+=nums[i]

            if curr_sum in mydict:
                max_len=max(max_len,i-mydict[curr_sum])

            else:
                mydict[curr_sum]=i
        return max_len