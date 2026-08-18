class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        max_num=float('-inf')
        min_num=float('inf')
        high=-1
        low=-1

        for i in range(0,len(nums)):
            if nums[i]>=max_num:
                max_num=nums[i]
            else:
                high=i
        for j in range(len(nums)-1,-1,-1):
            if nums[j]<=min_num:
                min_num=nums[j]
            else:
                low=j
        if low==-1:
            return 0
        return high-low+1