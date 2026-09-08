class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        left_pro=1
        right_pro=1
        max_pro=float("-inf")

        for i in range(len(nums)):
            left_pro*=nums[i]
            right_pro*=nums[len(nums)-i-1]

            max_pro=max(max_pro,left_pro,right_pro)
            
            if left_pro==0:
                left_pro=1
            if right_pro==0:
                right_pro=1
        return max_pro