class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def concatenate(self, other_list):
        if not self.head:
            self.head = other_list.head
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = other_list.head

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Ejemplo de uso
list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(3)

list2 = LinkedList()
list2.append(4)
list2.append(5)
list2.append(6)

print("Lista 1:")
list1.print_list()

print("Lista 2:")
list2.print_list()

list1.concatenate(list2)

print("Lista concatenada:")
list1.print_list()
# Crear una tercera lista concatenada
list3 = LinkedList()

# Concatenar la primera lista a la tercera lista
list3.concatenate(list1)

# Concatenar la segunda lista a la tercera lista
list3.concatenate(list2)

print("Tercera lista concatenada:")
list3.print_list()