class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        if len(s)==1:
            return False
        for i in s:
            if i==")":
                if stack:
                    if stack[-1]=="(" and i==")":
                        stack.pop()
                    else:
                        stack.append(i)    
                else:
                    stack.append(i)
            elif i=="]":
                if stack:
                    if stack[-1]=="[" and i=="]":
                        stack.pop()
                    else:
                        stack.append(i)    
                else:
                    stack.append(i)    
            elif i=="}":
                if stack:
                    if stack[-1]=="{" and i=="}":
                        stack.pop()
                    else:
                        stack.append(i)    
                else:
                    stack.append(i)    
            else:
                stack.append(i)
        if len(stack) == 0:
            return True
        return False
                
        