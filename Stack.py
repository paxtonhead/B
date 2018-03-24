#Team Crab

from Deque import Deque

class Stack:

    def __init__(self):
        self._dq = Deque()

    def __str__(self):
        return str(self._dq)
        pass

    def __len__(self):
        return len(self._dq)
        pass

    def push(self, val):
        self._dq.push_front(val)
        pass

    def pop(self):
        return self._dq.pop_front()
        pass

    def peek(self):
        return self._dq.peek_front()
        pass

if __name__ == '__main__':
    pass #Unit tests make this unnecessary