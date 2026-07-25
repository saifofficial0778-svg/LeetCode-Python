class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()

        while n!=1:
            seen.add(n)
            sum=0
            while n>0:
                ld=n%10
                sum+=ld*ld
                n=n//10

            n=sum

            if sum in seen:
                return False
        return True