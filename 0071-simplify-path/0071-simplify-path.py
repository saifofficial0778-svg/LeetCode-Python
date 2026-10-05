class Solution:
    def simplifyPath(self, path: str) -> str:
        ans=path.split('/')
        stack=[]

        for ch in ans:
            if ch=="" or ch==".":
                continue
            elif ch=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        res="/"+"/".join(stack)
        return res