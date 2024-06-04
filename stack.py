class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)


    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Error: Stack is empty")


    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Error: Stack is empty")


    def size(self):
        return len(self.items)



stack = Stack()

##is_empty
#print(stack.is_empty())
#stack.push(5)
#stack.push(6)
#stack.push(7)
#stack.push("ruchka")
#stack.push(9)
##xamma elementlarni birdaniga chiqaradi
#print(stack.items)

##FIFO, Queue malumot tuzulmasi
#for i in stack.items:
#    print(i)

##LIFO,  Stack malumot tuzulmasi
#malumot = stack.items
#for i in stack.items[-1::-1]:
#    print(i)




#stack.push(12)
#print(stack.items)
#stack.push(13)
#print(stack.items)
#stack.push("gun")
#print(stack.items)
#stack.push(33)
#print(stack.items)
#stack.push('rrr')
#print(stack.items)
##o'chirib tashlamasdan ko'rish:peek
#print(stack.peek())



##size
#print(stack.items, stack.size())
#stack.push(422)
#print(stack.items, stack.size())
#stack.push("gunship")
#print(stack.items, stack.size())
#stack.push(427)
#print(stack.items, stack.size())
#stack.push('rrr')
#print(stack.items, stack.size())
#stack.push(272)
#print(stack.items, stack.size())
#stack.push('run')
#print(stack.items, stack.size())
#stack.push(747)
#print(stack.items, stack.size())


##pop
#stack.push(57)
#stack.push(58)
#stack.push(67)
#stack.push(86)
#stack.push(96)
#stack.push(231)
#stack.push(43)
#print("Stack before:", stack.items)
#top_item = stack.pop()
#print("Propped:", top_item)
#print("Stack after pop:", stack.items)



##peek
#stack.push(57)
#stack.push(58)
#stack.push(67)
#stack.push(86)
#stack.push(96)
#stack.push(231)
#stack.push(43)
#print("Stack before:", stack.items)
#peeked_item = stack.peek()
#print("Peeked:", peeked_item)
#print("Stack after:", stack.items)

