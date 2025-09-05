class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        xx = Doubly_Linked_List_Node(x)
        if self.head == None:
            self.tail = xx
        else:
            self.head.prev = xx
        xx.next = self.head
        xx.prev = None
        self.head = xx

    def insert_last(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        xx = Doubly_Linked_List_Node(x)
        if self.tail == None:
            self.head = xx
        else:
            self.tail.next = xx
        xx.prev = self.tail
        xx.next = None
        self.tail = xx

    def delete_first(self):
        x = self.head
        if x.next == None:
            self.head = None
            self.tail = None
        else:
            self.head = x.next
            x.next = None
            self.head.prev = None
        x.prev = None
        return x.item

    def delete_last(self):
        x = self.tail
        if x.prev == None:
            self.head = None
            self.tail = None
        else:
            self.tail = x.prev
            x.prev = None
            self.tail.next = None
        x.next = None
        return x.item

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        ###########################
        # Part (b): Implement me! # 
        ###########################
        a = x1.prev
        b = x2.next
        a.next = b
        b.prev = a
        x1.prev = None
        x2.next = None
        L2.head = x1
        L2.tail = x2
        return L2

    def splice(self, x, L2):
        ###########################
        # Part (c): Implement me! # 
        ###########################
        y = x.next
        x.next = L2.head
        y.prev = L2.tail
        L2.head.prev = x
        L2.tail.next = y
        L2.head = None
        L2.tail = None
        return L2
    def output(self):
        cur = self.head
        string = ""
        while cur != None:
            string += str(cur.item) + " "
            cur = cur.next
        print(string)

def main():
    L1 = Doubly_Linked_List_Seq()
    L1.insert_first(7)
    L1.insert_first(6)
    L1.insert_first(5)
    L1.insert_first(4)
    L1.insert_first(3)
    L1.insert_first(2)
    L1.insert_first(1)
    L1.output()
    L1.delete_first()
    L1.delete_last()
    L1.output()
    L1.remove(L1.head.next, L1.tail.prev.prev)
    L1.output()
    L2 = Doubly_Linked_List_Seq()
    L2.insert_first(4)
    L2.insert_first(3)
    L1.splice(L1.head, L2)
    L1.output()

if __name__ == "__main__":
    main()