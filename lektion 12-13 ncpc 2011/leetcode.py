class LeetCode:

    def __init__(self):
        super().__init__()
        self._parentheses = list()
        self._result = list()
    
    def opg(self, n):
        
        self.makeParentheses(n)
        for i in range(len(self._parentheses)-1):
            for j in range(len(self._parentheses)-1):
                self.swap(i,j)

                if self.isValid():
                    if self._result.count(("".join(self._parentheses))) == 0:
                        self._result.append("".join(self._parentheses))

        return self._result

    def makeParentheses(self, n):
        
        for i in range(n):
            self._parentheses.append("(")
            self._parentheses.append(")")
    
    def swap(self, pos1, pos2):
        temp = self._parentheses[pos1]
        self._parentheses[pos1] = self._parentheses[pos2]
        self._parentheses[pos2] = temp
    
    def isValid(self):
        stack = []
        for i in self._parentheses:
            if i == '(':
                stack.append(i)
            else:
                try:
                    stack.pop(len(stack)-1)
                except:
                    return False
        
        if len(stack) > 0:
            return False
        else:
            return True

        
    

lc = LeetCode()

for i in lc.opg(3):
        print(i)
