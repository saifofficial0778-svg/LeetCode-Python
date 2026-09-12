class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mydict={0:1}
        count=0
        curr_sum=0
        
        for num in nums:
            curr_sum+=num

            rem=curr_sum%k
            
            if rem in mydict:
                count+=mydict[rem]

            mydict[rem]=mydict.get(rem,0)+1

        return count