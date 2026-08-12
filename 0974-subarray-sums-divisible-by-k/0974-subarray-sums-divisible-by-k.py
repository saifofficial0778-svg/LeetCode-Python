class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count=0
        mydict={0:1}
        curr_sum=0

        for i in range(len(nums)):
            curr_sum+=nums[i]

            rem = curr_sum % k
            if rem in mydict:
                count+=mydict[rem]
            if rem not in mydict:
                mydict[rem]=1
            else:
                mydict[rem]+=1
        return count
