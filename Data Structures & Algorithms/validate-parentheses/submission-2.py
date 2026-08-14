class Solution:
    def isValid(self, s: str) -> bool:
        #thinks to rembr,,,, if stack not empty at the end, nuh uh
        #the idea here is tht every open bracket gets pushed to the stack
        #if we encounter a closing bracket check stack[-1]and see if its equal 
        #equal as in gets matched w the hashmap value

        stack = []
        m = {')':'(','}':'{',']':'['}
        for c in s:
            if c in m:
                if stack and stack[-1] == m[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        else:
            return False                
