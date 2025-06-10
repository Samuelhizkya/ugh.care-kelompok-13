# Membuat Class Node
class Node:
    def __init__(self,data):
        self._data = data
        self._next = None

 # Membuat Class LL (Linkedlist)    
class LL:
    def __init__(self):
        self._head = None
    
     # Membuat Method Prepend
    def prepend(self, data):
        a = Node(data) 
        if self._head == None: 
            self._head = a 
        else:
            a._next = self._head 
            self._head = a 
            
     # Membuat Method append
    def append(self, data):
        a = Node(data) 
        if not self._head:  
            self._head = a 
            return 
        last_node = self._head 
        while last_node._next: 
            last_node = last_node._next
        last_node._next = a 
    

    def hapus(self, data):
        current = self._head 
        prev = None 

        while current: 
            if current._data == data: 
                if prev:  
                    prev._next = current._next 
                else:  
                    self._head = current._next
                return  
            prev = current
            current = current._next

    def display(self):
        a = self._head 
        while a != None: 
            print(a._data, end=" -> ") 
            a = a._next 
        print("None")

# Penggunaan
myLL = LL()
myLL.display()