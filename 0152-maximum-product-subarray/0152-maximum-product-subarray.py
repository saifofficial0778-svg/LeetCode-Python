class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        left_pro=1
        right_pro=1
        n=len(nums)
        max_left=float('-inf')
        max_right=float('-inf')
        for i in range(n):
            left_pro*=nums[i]

            max_left=max(max_left,left_pro)
            if left_pro==0:
                left_pro=1

        for i in range(n-1,-1,-1):
            right_pro*=nums[i]

            max_right=max(max_right,right_pro)
            if right_pro==0:
                right_pro=1
        return max(max_right,max_left)
        
            
