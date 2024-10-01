# Node class to represent each node in the circular doubly linked list
class Node:
    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.prev = None  # Pointer to the previous node
        self.next = None  # Pointer to the next node

# Circular Doubly Linked List class
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None  # Head of the linked list

    # Function to add a node at the end of the circular list
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            last = self.head.prev
            last.next = new_node
            new_node.prev = last
            new_node.next = self.head
            self.head.prev = new_node

    # Function to print the circular linked list
    def print_list(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print()

    # Function to delete a node
    def delete_node(self, key):
        if self.head is None:
            return
        curr = self.head
        prev_node = None

        # If the node to be deleted is the head
        while curr.data != key:
            if curr.next == self.head:
                print("Node not found")
                return
            prev_node = curr
            curr = curr.next

        if curr.next == self.head and prev_node is None:
            self.head = None
        elif curr == self.head:
            prev_node = self.head.prev
            self.head = curr.next
            prev_node.next = self.head
            self.head.prev = prev_node
        elif curr.next == self.head:
            prev_node.next = self.head
            self.head.prev = prev_node
        else:
            temp = curr.next
            prev_node.next = temp
            temp.prev = prev_node
        curr = None

# Example usage:
cdll = CircularDoublyLinkedList()

cdll.append(1)
cdll.append(2)
cdll.append(3)
cdll.append(4)
cdll.append(5)

print("Circular Doubly Linked List:")
cdll.print_list()

# Deleting a node
cdll.delete_node(3)
print("After deleting node 3:")
cdll.print_list()
