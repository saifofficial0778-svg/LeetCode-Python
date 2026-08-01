class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_sum=-1
        n=len(height)
        left=0
        right=n-1
        while left<right:
            if height[right]>height[left]:
                sum=min(height[left],height[right])*(right-left)
                max_sum=max(max_sum,sum)
                left+=1
            else:
                sum=min(height[left],height[right])*(right-left)
                max_sum=max(max_sum,sum)
                right-=1
        
                
        return max_sum