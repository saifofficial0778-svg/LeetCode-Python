class Solution:
    def isValid(self, s: str) -> bool:
        pairs={
            ')':'(',
            '}':'{',
            ']':'['
        }

        stack=[]
        
        for ch in s:
            if ch not in pairs:
                stack.append(ch)
            else:
                if not stack:
                    return False
                if stack[-1]!=pairs[ch]:
                    return False
                stack.pop()
        return len(stack)==0
            
        
            