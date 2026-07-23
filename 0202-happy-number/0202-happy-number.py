class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        
        while n!=1 and n not in seen:
            seen.add(n)
            sum=0

            while n>0:
                last_digit=n%10
                sum+=last_digit*last_digit
                n=n//10
            n=sum
        return n == 1

           
           
        
