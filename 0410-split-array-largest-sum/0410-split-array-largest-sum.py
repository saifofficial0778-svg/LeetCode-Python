class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        low,high=max(nums),sum(nums)

        while low<high:
            sub_arr=(low+high)//2

            count=1
            sub_sum=0
            for num in nums:
                sub_sum+=num
                if sub_sum>sub_arr:
                    count+=1
                    sub_sum=num
            
            if count<=k:
                high=sub_arr
            else:
                low=sub_arr+1

        return low

