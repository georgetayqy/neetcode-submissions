from collections import deque

class MyStack:

    def __init__(self):
        self.first = deque()
        self.second = deque()


    def push(self, x: int) -> None:
        self.first.appendleft(x)

    def pop(self) -> int:
        while len(self.first) > 1:
            self.second.appendleft(self.first.pop())
        to_return = self.first.pop()
        self.first, self.second = self.second, self.first

        return to_return

    def top(self) -> int:
        return self.first[0]

    def empty(self) -> bool:
        return len(self.first) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()