class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mydict={0:1}
        count=0
        curr_sum=0
        for i in range(len(nums)):
            curr_sum+=nums[i]
            if curr_sum-k in mydict:
                count+=mydict[curr_sum-k]
            if curr_sum not in mydict:
                mydict[curr_sum]=1
            else:
                mydict[curr_sum]+=1
        return count

