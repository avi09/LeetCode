class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        answer = 0
        sign = "+"
        buffer = "0"

        def doit(sign, answer1, answer2):
            if sign == "+":
                return int(answer1) + int(answer2)
            else:
                return int(answer1) - int(answer2)

        for i in range(len(s)):
            if s[i].isdigit():
                buffer += s[i]
            elif s[i] == "+" or s[i] == "-" :
                answer = doit(sign, answer, buffer)
                buffer = "0"
                sign = s[i]
            elif s[i] == "(":
                stack.append((answer, sign))
                answer = 0
                sign = "+"
                buffer = ""
            elif s[i] == ")":
                answer = doit(sign, answer, buffer)
                answer = doit(stack[-1][1], stack[-1][0], answer)
                stack = stack[:-1]
                buffer = "0"
        answer = doit(sign, answer, buffer)
        return answer
        
