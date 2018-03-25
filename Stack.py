#Team Crab

class Linked_List:
    class _Node:

        def __init__(self, val):
            # declare and initialize the private attributes
            # for objects of the Node class.
            self._next = None
            self._prev = None
            self._value = val

    def __init__(self):
        # declare and initialize the private attributes
        # for objects of the sentineled Linked_List class
        self._header = self._Node(None)  # added self for Nodes
        self._trailer = self._Node(None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._header._prev = None
        self._trailer.next = None
        self._size = 0

    def __len__(self):
        # return the number of value-containing nodes in
        # this list.
        return self._size

    def append_element(self, val):
        # increase the size of the list by one, and add a
        # node containing val at the new tail position. this
        # is the only way to add items at the tail position.
        newest = self._Node(val)
        current = self._trailer._prev
        newest._prev = current
        newest._next = self._trailer
        current._next = newest
        self._trailer._prev = newest
        self._size += 1

    def insert_element_at(self, val, index):
        # assuming the head position (not the header node)
        # is indexed 0, add a node containing val at the
        # specified index. If the index is not a valid
        # position within the list, raise an IndexError
        # exception. This method cannot be used to add an
        # item at the tail position.
        if index < 0 or index >= self._size:
            raise IndexError
        elif index == self._size:
            self.append_element(val)
        else:
            newest = self._Node(val)
            current = self._header
            for k in range(index):
                current = current._next
            newest._next = current._next
            newest._prev = current
            current._next._prev = newest
            current._next = newest
            self._size += 1

    def remove_element_at(self, index):
        # assuming the head position (not the header node)
        # is indexed 0, remove and return the value stored
        # in the node at the specified index. If the index
        # is invalid, raise an IndexError exception.
        if index < 0 or index >= self._size or self._size == 0:
            raise IndexError
        else:
            current = self._header
            for k in range(index):
                current = current._next
            to_return = current._next._value
            current._next = current._next._next
            current._next._prev = current
            self._size -= 1
            return to_return

    def swap(self, index1, index2):
        if index1 == index2:
            return
        current = self._header
        for i in range(index1 + 1):
            current = current._next
        current2 = self._header
        for i in range(index2 + 1):
            current2 = current2._next
        temp = current._value
        current._value = current2._value
        current2._value = temp

    def get_element_at(self, index):
        # assuming the head position (not the header node)
        # is indexed 0, return the value stored in the node
        # at the specified index, but do not unlink it from
        # the list. If the specified index is invalid, raise
        # an IndexError exception.
        if index < 0 or index > self._size - 1 or self._size == 0:
            raise IndexError
        else:
            current = self._header
            for k in range(index + 1):
                current = current._next
            return current._value

    def remove_element(self, value):
        current = self._header
        for i in range(len(self)):
            if current._value == value:
                current._prev._next = current._next
                current._next._prev = current._prev
                return
            current = current._next

    def __str__(self):
        # return a string representation of the list's
        # contents. An empty list should appear as [ ].
        # A list with one element should appear as [ 5 ].
        # A list with two elements should appear as [ 5, 7 ].
        # You may assume that the values stored inside of the
        # node objects implement the __str__() method, so you
        # call str(val_object) on them to get their string
        # representations.
        if self._size == 0:
            return "[ ]"
        elif self._size == 1:
            current = self._header._next
            return "[ " + str(current._value) + " ]"
        else:
            current = self._header._next
            to_return = "[ "
            while current._next != self._trailer:
                to_return += str(current._value) + ", "
                current = current._next
            to_return += str(current._value) + " ]"
            return to_return

    def __iter__(self):
        # initialize a new attribute for walking through your list
        # TODO insert your initialization code before the return
        # statement. do not modify the return statement.
        self._iter_index = 0
        self._iter_var = self._header._next
        return self

    def __next__(self):
        # using the attribute that you initialized in __iter__(),
        # fetch the next value and return it. If there are no more
        # values to fetch, raise a StopIteration exception.
        if self._iter_index == self._size:
            raise StopIteration
        to_return = self._iter_var._value
        self._iter_var = self._iter_var._next
        self._iter_index = self._iter_index + 1
        return to_return


class Deque:

    def __init__(self):
        self._list = Linked_List()

    def __str__(self):
        return str(self._list)

    def __len__(self):
        return len(self._list)

    def push_front(self, val):

        if len(self._list) == 0:
            self._list.append_element(val)

        else:
            self._list.insert_element_at(val, 0)
        pass

    def pop_front(self):
        if len(self) <= 0:
            return None
        return self._list.remove_element_at(0)
        pass

    def peek_front(self):
        if len(self) <= 0:
            return None
        return self._list.get_element_at(0)
        pass

    def push_back(self, val):
        self._list.append_element(val)
        pass

    def pop_back(self):
        if len(self) <= 0:
            return None
        return self._list.remove_element_at(len(self._list) - 1)
        pass

    def peek_back(self):
        if len(self) <= 0:
            return None
        return self._list.get_element_at(len(self._list) - 1)
        pass

    def is_empty(self):
        return len(self) == 0


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