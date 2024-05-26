class MyQueue:

    def __init__(self):
        self.s1 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        n = len(self.s1)
        for i in range(n - 1, -1, -1):
            self.s2.append(self.s1.pop())

        val = self.s2.pop()

        for i in range(n - 2, -1, -1):
            self.s1.append(self.s2.pop())
        return val

    def peek(self) -> int:
        return self.s1[0]

    def empty(self) -> bool:
        n = len(self.s1)
        if n == 0:
            return True

        return False
