class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
    def __str__(self):
        return "Node({})".format(self.value)
     
    __repr__ = __str__
 
 
class Stack:
    def __init__(self):
        self.top = None
        self.count = 0
        self.minimum = None
         
    def __str__(self):
        temp = self.top
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = '\n'.join(out)
        return ('Top {} \n\nStack :\n{}'.format(self.top,out))

    __repr__=__str__
     
    def getMin(self):
        if self.top is None:
            return "Stack is empty"
        else:
            print("Minimum Element in the stack is: {}" .format(self.minimum))
 
