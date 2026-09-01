class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
            stk = []
            #["4","13","5","/","+"]

            #4+13/5

            # tokens.reverse()

            for i in tokens:
                if i == '+':
                    a = stk.pop()
                    b = stk.pop()
                    stk.append(a+b)
                elif i == '-':
                    a = stk.pop()
                    b = stk.pop()
                    stk.append(b-a)

                elif i == '*':
                    a = stk.pop()
                    b = stk.pop()
                    stk.append(a*b)
                elif i == '/':
                    a = stk.pop()
                    b = stk.pop()
                    stk.append(int(b / a))
                else:
                    stk.append(int(i))
  
            return stk.pop()
