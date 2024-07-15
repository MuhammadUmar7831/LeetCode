class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = None #global min for stack
        

    def push(self, val):
        if self.min == None: #min is val if stack is empty or nmin is None ( min is None when stack is empty )
            self.min = val
        elif self.min > val:
            self.min = val
        
        self.stack.append([val, self.min])
        """
        :type val: int
        :rtype: None
        """
        

    def pop(self): # pop last element and update global min
        self.stack.pop(len(self.stack)-1)
        if len(self.stack) > 0:
            self.min = self.stack[len(self.stack)-1][1]
        else:
            self.min = None
        """
        :rtype: None
        """
        

    def top(self): # return last element
        return self.stack[len(self.stack)-1][0]
        """
        :rtype: int
        """
        

    def getMin(self): # return min of top
        return self.stack[len(self.stack)-1][1]
        """
        :rtype: int
        """
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()