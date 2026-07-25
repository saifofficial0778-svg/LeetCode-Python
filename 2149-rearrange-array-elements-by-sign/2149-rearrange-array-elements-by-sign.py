class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        pos_idx=0
        neg_idx=1

        for num in nums:
            if num>0:
                res[pos_idx]=num
                pos_idx+=2
            else:
                res[neg_idx]=num
                neg_idx+=2
        return res
        

       
