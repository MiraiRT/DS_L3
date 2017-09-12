class Queue:
    def __init__(self):
        self.items = []

    def enQueue(self, i):
        self.items.append(i)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def deQueue(self):
        self.items.pop(0)


# 1
print('NO.1')
q1 = Queue()
q1.enQueue('A')
print(q1.items)
q1.enQueue('B')
print(q1.items)
q1.enQueue('C')
print(q1.items)

# 2.1
print('\n' + 'NO. 2.1')
q2 = Queue()
name = 'Rachata'
for i in range(len(name)):
    q2.enQueue(name[i])

print(q2.items)
for i in range(len(name)):
    print(name[i], end='')

# 2.2
print('\n\n' + 'NO. 2.2')
q3 = Queue()
print("There is the queue >> " + str(q3.isEmpty()))
print(q3.size())
q3.enQueue('A')
print(q3.items, end='')
print(" >> " + str(q3.size()))
q3.enQueue('B')
q3.enQueue('C')
print(q3.items, end='')
print(" >> " + str(q3.size()))
print("There is the queue >> " + str(q3.isEmpty()) + "\n")
for i in range(len(q3.items)):
    q3.deQueue()
    print(q3.items, end='')
    print(" >> " + str(q3.size()))
    print("There is the queue >> " + str(q3.isEmpty()))

