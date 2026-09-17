class Solution:
    def simplifyPath(self, path: str) -> str:
        res=path.split('/')
        stack=[]

        for ch in res:
            if ch=='.' or ch=='':
                continue
            elif ch=='..':
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        return '/'+'/'.join(stack)

