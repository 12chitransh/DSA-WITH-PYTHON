class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next


class DLL:
    def __init__(self, head=None):
        self.head = head

    def i_beg(self, value):
        n = Node(None, value, self.head)

        if self.head is not None:
            self.head.prev = n

        self.head = n

    def i_end(self, value):
        n = Node(None, value, None)

        if self.head is None:
            self.head = n
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = n
        n.prev = temp

        
    def i_mid(self, target, value):
        temp = self.head

        while temp is not None and temp.item != target:
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        n = Node(temp, value, temp.next)

        if temp.next is not None:
            temp.next.prev = n

        temp.next = n

    def d_beg(self):
        if self.head is None:
            print("underflow")
            return

        if self.head.next is None:
            self.head = None
            return

        self.head = self.head.next
        self.head.prev = None

    def d_end(self):
        if self.head is None:
            print("underflow")
            return 

        if self.head.next is None:
            self.head = None
            return 

        temp = self.head 
        while temp.next is not None:
            temp = temp.next 

        prev_node = temp.prev
        prev_node.next = None

    def d_mid(self, target):
        if self.head is None:
            print("underflow")
            return

        temp = self.head

        # Search node
        while temp is not None and temp.item != target:
            temp = temp.next

        # Value not found
        if temp is None:
            print("Value not found")
            return

        # Case 1: first node
        if temp.prev is None:
            self.head = temp.next
            if self.head is not None:
                self.head.prev = None
            return

        # Case 2: last node
        if temp.next is None:
            temp.prev.next = None
            return

        # Case 3: middle node
        temp.prev.next = temp.next
        temp.next.prev = temp.prev




        

