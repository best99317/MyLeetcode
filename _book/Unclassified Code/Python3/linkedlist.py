class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext


class linkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, val):
        temp = Node(val)
        temp.setNext(self.head) # temp.next = self.head
        self.head = temp

    def length(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.getNext() # cur = cur.next
        return count

    def search(self, target):
        cur = self.head
        while cur:
            if cur.getData() != target:  # cur.val != target
                cur = cur.getNext() # cur = cur.next
            else:
                return True
        return False

    def remove(self, target):
        cur = self.head
        previous = None
        while cur:
            if cur.getData() != target:
                previous = cur
                cur = cur.getNext()
            else:
                if cur == self.head:
                    self.head = cur.getNext()
                    return
                else:
                    previous.setNext(cur.getNext())
                    return

    def append(self, data):
        temp = Node(data)
        temp.setNext(self.head)
        self.head = temp

    def insert(self, tar_pos, data):
        cur = self.head
        cur_pos = 0
        previous = None
        while cur_pos < tar_pos:
            previous = cur
            cur = cur.getNext()
            cur_pos += 1
        newNode = Node(data)
        newNode.setNext(cur)
        if tar_pos == 0:
            self.head = newNode
        else:
            previous.setNext(newNode)


    def index(self, target):
        cur = self.head
        index = 0
        while cur:
            if cur.getData() == target:
                return index
            else:
                cur = cur.getNext()
                index += 1
        return -1

    def pop(self, index):
        if index == 0:
            pop = self.head.getData()
            self.head.setNext(self.head.getNext().getNext())
            return pop
        else:
            cur = self.head
            previous = None
            cur_pos = 0
            while cur_pos < index:
                previous = cur
                cur = cur.getNext()
                cur_pos += 1
            pop = cur.getData()
            previous.setNext(cur.getNext())
            return pop

mylist = linkedList()
mylist.add(31)
mylist.add(77)
mylist.add(89)
print(mylist.search(76))
mylist.add(76)
print(mylist.search(31))
print(mylist.search(89))
mylist.remove(76)
mylist.append(75)
mylist.insert(2,76)
a = mylist.index(89)
mylist.pop(1)