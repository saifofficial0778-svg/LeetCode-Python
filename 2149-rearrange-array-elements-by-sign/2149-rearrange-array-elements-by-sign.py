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
        p1=0
        p2=0
        res=[0]*n
        for i in range(0,n):
            if i%2==0:
                res[i]=pos[p1]
                p1+=1
            else:
                res[i]=neg[p2]
                p2+=1
        return res

       
