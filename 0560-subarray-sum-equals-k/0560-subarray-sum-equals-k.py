class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mydict={0:1}
        count=0
        sum=0

        for i in range(0,len(nums)):
            sum+=nums[i]

            if sum-k in mydict:
                count+=mydict[sum-k]

            if sum not in mydict:
                mydict[sum]=1
            else:
                mydict[sum]+=1
        return count
