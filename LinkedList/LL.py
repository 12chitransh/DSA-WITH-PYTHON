class Node :
    def __init__(self , item , next=None):
        self.item = item,
        self.next = next

class SLL :
    def __init__(self , head=None):
        self.head = head

    def i_end(self, value):
        n = Node(value)

        if self.head == None:
            self.head = n
            return

        temp = self.head
        while temp.next != None:
            temp = temp.next

        temp.next = n

    def i_start(self , value):
        n = Node(value)
        if self.head == None :
            self.head = n
            return 
        n.next = self.head 
        self.head = n
         
    def i_mid(self, value, data):
        n = Node(value)
        temp = self.head

        while temp != None and temp.item != data:
            temp = temp.next

        if temp == None:
            print("Value not found")
            return

        n.next = temp.next
        temp.next = n

    def d_end(self):
        if self.head == None:
            print("Nothing found")
            return


        if self.head.next == None:
            self.head = None
            return

        temp = self.head
        prev = None

        while temp.next != None:
            prev = temp
            temp = temp.next

        prev.next = None

    def d_beg(self):
        if self.head == None:
            print("Nothing Found")
            return 

        self.head = self.head.next

    def d_mid(self, data):
        if self.head == None:
            print("Nothing Found")
            return 

        temp = self.head
        prev = None

        while temp != None and temp.item != data:
            prev = temp
            temp = temp.next

        if temp == None:
            print("Value not found")
            return

        if prev == None:
            self.head = temp.next
        else:
            prev.next = temp.next

    def printLL(self):
        temp = self.head

        if temp == None:
            print("List is empty")
            return

        while temp != None:
            print(temp.item)
            temp = temp.next


obj = SLL()
obj.i_start(10)
obj.i_start(1)
obj.i_end(20)
obj.printLL() 
print(obj,end=" ")           

            
        


            