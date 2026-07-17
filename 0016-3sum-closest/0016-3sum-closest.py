class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_sum = nums[0] + nums[1] + nums[2]
        nums.sort()
        n=len(nums)
        for i in range(0,n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=n-1

            while left< right:
                curr_sum=nums[i]+nums[left]+nums[right]

                if curr_sum==target:
                    return curr_sum
                if abs(curr_sum-target)<abs(closest_sum-target):
                    closest_sum=curr_sum
                if curr_sum<target:
                    left+=1
                else:
                    right-=1
        return closest_sum
