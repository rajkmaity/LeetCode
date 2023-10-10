class Solution:
    def isValid(self, s: str) -> bool:
        stack=[] # just for append and pop
        pairs={
            '(':')',
            '{':'}',
            '[':']'
        }
        for b in s:
            if b in pairs:
                stack.append(b)
            elif len(stack) ==0 or b != pairs[stack.pop()]:
                return False
        return len(stack) ==0
