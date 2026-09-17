class Solution:
    def simplifyPath(self, path: str) -> str:
        paths=path.split('/')
        stack=[]
        for ch in paths:
            if ch=='.' or ch=='':
                continue
            elif  ch=='..':
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        return "/"+"/".join(stack)
