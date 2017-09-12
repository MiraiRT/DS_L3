class Queue:
    def __init__(self):
        self.items = []

    def enQueue(self, i):
        self.items.append(i)

    def size(self):
        return len(self.items)

    def deQueue(self):
        return self.items.pop(0)


isr = Queue()
en = Queue()


def cc(c, n):  # Convert Character #
    if 64 < ord(c) + n < 91 or 96 < ord(c) + n < 123:
        return chr(ord(c) + n)
    else:
        return chr(ord(c) + n)


def encode():
    es = input("Enter Encoded Message : ")
    for i in range(len(es)):
        en.enQueue(es[i])
    ns = input("Enter I-Series Number : ")
    for i in range(len(ns)):
        isr.enQueue(int(ns[i]))


def decode():
    s = ''
    while en.size() != 0:
        temp = isr.deQueue()
        s = s + cc(en.deQueue(), temp)
        isr.enQueue(temp)
    print('Decoded Message : ' + s)


encode()
decode()
