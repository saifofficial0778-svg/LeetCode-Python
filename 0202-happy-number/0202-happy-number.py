class Solution:
    def isHappy(self, n: int) -> bool:
        res=list()

        while n>=1 and n not in res:
            res.append(n)
            curr_sum=0
            while n>=1:
                ld=n%10
                curr_sum+=ld*ld
                n=n//10
            n=curr_sum
        return n==1
