class PythonListQueue(object):
    """
    A queue based on the built in Python list type.
    """
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        return self._items.pop(0)

    def size(self):
        return len(self._items)

    def is_empty(self):
        return len(self._items) == 0


class LinkedListNode(object):
    """
    A doubly linked list node, support for the LinkedListQueue. You should not need
    to change this code, but you will want to use it in the LinkedListQueue
    """
    def __init__(self, value, prevNode, nextNode):
        self.value = value
        self.prev = prevNode
        self.next = nextNode



class LinkedListQueue(object):
    """
    Finish the functions below to create a queue based on a linked list. Because
    a queue must either:

        * enqueue to the head and dequeue from the tail; or
        * enqueue to the tail and dequeue from the head.

    You should use a doubly linked list to ensure O(1) time enqueue and dequeue.
    """
    def __init__(self):
        self.start = LinkedListNode(None, None, None)
        self.end = LinkedListNode(None, self.start, None)
        self.start.next = self.end
        self._size = 0

    def enqueue(self, item):
        self._size += 1
        new_node = LinkedListNode(item, None, None)
        prev_end = self.end.prev
        prev_end.next = new_node
        self.end.prev = new_node

        new_node.prev = prev_end
        new_node.next = self.end

    def dequeue(self):
        if self.size() > 0:
            self._size -= 1
            first_node = self.start.next
            next_start = first_node.next
            self.start.next = next_start
            next_start.prev = self.start
            return first_node.value
        else:
            raise("queue is empty")

    def size(self):
        return self._size

    def is_empty(self):
        return self.size() == 0


class RingBufferQueue(object):
    """
    Finish the functions below such that this queue is backed by a Ring Buffer.
    Recall that a ring buffer uses an array and two pointers to keep track of
    where to read, and where to write.

    Be careful! If the read pointer were to overtake the write pointer, it
    would return incorrect data! If the write pointer were to overtake the read
    pointer, it would overwrite data that hasn't been read yet!

    In many contexts, you would avoid this issue by stalling when one pointer
    would overwrite the other. Since doing so only makes sense in a multithreaded
    environment, you may prefer to just resize the underlying ring buffer at
    these times, instead.
    """
    def __init__(self):
        self._size = 0
        self.buffer_size = 16
        self.reset_pointers()
        self.initialize_buffer()

    def enqueue(self, item):
        if self.size() == self.buffer_size:
            self.resize()

        self._size += 1
        self.buffer[self.write_index] = item
        self.write_index = (self.write_index + 1) % self.buffer_size

    def dequeue(self):
        if self.is_empty():
            raise("Empty queue")
        else:
            self._size -= 1
            item = self.buffer[self.read_index]
            self.read_index = (self.read_index + 1) % self.buffer_size
            return item

    def resize(self):
        prev_items = []

        while self.size() > 0:
            prev_items.append(self.dequeue())

        self.buffer_size = self.buffer_size * 2
        self.initialize_buffer()
        self.reset_pointers()

        for item in prev_items:
            self.enqueue(item)

    def size(self):
        return self._size

    def is_empty(self):
        return self.size() == 0

    def initialize_buffer(self):
        self.buffer = [None] * self.buffer_size

    def reset_pointers(self):
        self.read_index = 0
        self.write_index = 0

QUEUE_CLASSES = (
    PythonListQueue,
    LinkedListQueue,
    RingBufferQueue
)

