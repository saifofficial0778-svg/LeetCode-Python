class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mydict={0:1}
        n=len(nums)
        curr_sum=0
        count=0
        for i in range(n):
            curr_sum+=nums[i]

            rem=curr_sum%k

            if rem in  mydict:
                count+=mydict[rem]
            if rem not in mydict:
                mydict[rem]=1
            else:
                mydict[rem]+=1
        return count

            