class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0


    def enqueue(self, item):
        self.items.append(item)


    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Error: Queue is empty")


    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Error: Queue is empty")


    def size(self):
        return len(self.items)


    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Error: Queue is_empty")




queue = Queue()

##is_empty
print(queue.items, queue.is_empty())
#queue.enqueue("lavash")
#queue.enqueue("Donar")
#queue.enqueue("Sendvich")
#queue.enqueue("Gamburger")
#queue.enqueue("Chizburger")
#print(queue.items, queue.is_empty())



##dequeue
#queue.enqueue("1 mijoz")
#print(queue.items)
#queue.enqueue("2 mojoz")
#queue.enqueue("3 mijoz")
#queue.enqueue("4 mijoz")
#queue.enqueue("5 mijoz")
#print(queue.items)
#queue.dequeue()
#print(queue.items)
#queue.dequeue()
#print(queue.items)


##peek
#queue.enqueue("1 mijoz")
#print(queue.items)
#queue.enqueue("2 mojoz")
#queue.enqueue("3 mijoz")
#queue.enqueue("4 mijoz")
#queue.enqueue("5 mijoz")
#print(queue.items)
#print(queue.peek())



##size
#queue.enqueue("lavash")
#queue.enqueue("Donar")
#queue.enqueue("Sendvich")
#queue.enqueue("Gamburger")
#queue.enqueue("Chizburger")
#print(queue.items)
#print(queue.size())




queue.enqueue("lavash")
queue.enqueue("Donar")
queue.enqueue("Sendvich")
queue.enqueue("Gamburger")
queue.enqueue("Chizburger")
print(queue.peek())


