class MinStack:

    def __init__(self):
        self.min_value = []
        self.stack = []

    def push(self, val: int) -> None:
        if not self.min_value:
            self.min_value.append(val)
        else:
            self.min_value.append(min(self.min_value[-1], val))
        
        self.stack.append(val)
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_value.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        
        return None

    def getMin(self) -> int:
        return self.min_value[-1]
