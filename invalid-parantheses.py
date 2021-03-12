answers = set()
correction = 0
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        def search(builder, index, stack, original):
            global answers
            if len(original) == index:
                if len(builder) == len(original) - correction:
                    if builder.count('(') ==  builder.count(')'):
                        answers.add(builder)
                else:
                    return
            else:
                if original[index] == '(':
                    search(builder+'(', index+1, stack+1, original)
                    search(builder, index+1, stack, original)
                elif original[index] == ')':
                    if stack > 0:
                        search(builder+')', index+1, stack-1, original)
                        search(builder, index+1, stack, original)
                    else:
                        search(builder, index+1, stack, original)
                else:
                    search(builder+original[index], index+1, stack, original)
        
        global answers, correction
        answers = set()
        
        x1 = 0
        x2 = 0
        for i in range(len(s)):
            if s[i] == '(':
                x1+=1
            if s[i] == ')':
                if x1 > 0:
                    x1 -= 1
                else:
                    x2 += 1
        correction = x1 + x2
        search("", 0, 0, s)
