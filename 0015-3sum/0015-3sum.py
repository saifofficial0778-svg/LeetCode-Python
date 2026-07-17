class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        nums.sort()
        n=len(nums)

        for i in range(0,n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            low=i+1
            high=n-1

            while low<high:
                total_sum=nums[i]+nums[low]+nums[high]

                if total_sum<0:
                    low+=1
                elif total_sum>0:
                    high-=1
                else:
                    ans.append([nums[i], nums[low], nums[high]])
                    low+=1
                    high-=1

                    while low < high and nums[low]==nums[low-1]:
                        low+=1
                    while low < high and nums[high]==nums[high+1]:
                        high-=1
        return ans