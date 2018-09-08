def reverse(list_):
    new_list = []
    while len(list_) > 0:
        new_list.append(list_.pop())

    return new_list


test_list = [1,2,3,4]
print("Reversing {} {}".format(str(test_list), reverse(test_list)))


class Queue:
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []


    def enqueue(self, item):
        self.stack_1.append(item)

    def dequeue(self):
        if len(self.stack_2) == 0:
            while len(self.stack_1 ) > 0:
                self.stack_2.append(self.stack_1.pop())
        return self.stack_2.pop()

    def size(self):
        return len(self.stack_1) + len(self.stack_2)

    def is_empty(self):
        return self.size() == 0



queue = Queue()
queue.enqueue(4)
print("Enqueue 4 size: {}".format(queue.size()))
queue.enqueue(5)
print("Enqueue 5 size: {}".format(queue.size()))
queue.enqueue(6)
print("Enqueue 6 size: {}".format(queue.size()))

print("Dequeue {}".format( queue.dequeue()))
print("Dequeue {}".format(queue.dequeue()))
print("Dequeue {}".format(queue.dequeue()))

print("Queue is empty {}", queue.is_empty())
