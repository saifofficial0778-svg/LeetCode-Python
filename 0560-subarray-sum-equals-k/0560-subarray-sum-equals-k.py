class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mydict={0:1}
        count=0
        n=len(nums)
        sum=0
        for i in range(n):
            sum+=nums[i]
            if sum-k in mydict:
                count+=mydict[sum-k]
            if sum not in mydict:
                mydict[sum]=1
            elif sum in mydict:
                mydict[sum]+=1

        return count

