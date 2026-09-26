class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        low,high=max(nums),sum(nums)

        while low<=high:
            mid=(low+high)//2

            curr_sum=0
            count=1

            for num in nums:
                curr_sum+=num

                if  curr_sum>mid:
                    count+=1
                    curr_sum=num

            if count<=k:
                high=mid-1
            else:
                low=mid+1
        return low