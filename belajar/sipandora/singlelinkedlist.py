class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DCLL:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def remove_duplicates(self):
        if not self.head:
            return
        
        seen = set()
        current = self.head
        to_remove = []
        
        # First pass to identify duplicates
        while True:
            if current.data in seen:
                to_remove.append(current)
            else:
                seen.add(current.data)
            
            current = current.next
            if current == self.head:
                break
        
        # Second pass to remove duplicates
        for node in to_remove:
            node.prev.next = node.next
            node.next.prev = node.prev
            if node == self.head:
                self.head = node.next

    def __str__(self):
        if not self.head:
            return "Empty List"
        
        nodes = []
        current = self.head
        while True:
            nodes.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        return " <-> ".join(nodes) + " <-> (head)"

# Contoh penggunaan
dcll = DCLL()
for num in [1, 2, 3, 2, 4, 3, 3]:
    dcll.append(num)

print("Sebelum:", dcll)
dcll.remove_duplicates()
print("Sesudah:", dcll)