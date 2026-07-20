class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=set()
        n=len(nums)
        nums.sort()

        for i in range(0,n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                
                left=j+1
                right=n-1

                while left<right:
                    sum=nums[i]+nums[j]+nums[left]+nums[right]

                    if sum==target:
                        result.add((nums[i],nums[j],nums[left],nums[right]))

                    if sum<target:
                        left+=1
                    else:
                        right-=1
        return [list(item) for item in result]
