class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum=0
        sum_of_arr=0
        for num in nums:
            sum_of_arr+=num
        for i in range(0,len(nums)):
            right_sum=sum_of_arr-left_sum-nums[i]

            if right_sum==left_sum:
                return i
            left_sum+=nums[i]
        return -1