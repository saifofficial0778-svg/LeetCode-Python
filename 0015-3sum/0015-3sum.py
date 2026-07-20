class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result=[]
        n=len(nums)
        nums.sort()

        for i in range(0,n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=n-1

            while left<right:
                sum=nums[i]+nums[left]+nums[right]

                if sum==0:
                    result.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1

                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                elif sum>0:
                    right-=1
                else:
                    left+=1
        return result