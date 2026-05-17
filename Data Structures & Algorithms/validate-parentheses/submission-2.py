class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        operators = {')':'(',']':'[','}':'{'}
        opens = ['(','[','{']
        for c in s:
            in_op = c
            if(c in opens):
                stack.append(c)
            else:
                if(len(stack)!=0):
                    out = stack.pop()
                    if(out!=operators[c]):
                        return False
                else:
                    return False
        if(len(stack)==0):
            return True    
        else:
            return False