class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        n=len(nums)

        for num in nums:
            if num>0:
                pos.append(num)
            else:
                neg.append(num)
       
        res=[0]*n
        res[0::2] = pos
        res[1::2] = neg
        return res

       
