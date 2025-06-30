class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        """Add a node with given data to the end of the list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        """Print all elements in the list"""
        if not self.head:
            print("List is empty.")
            return

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        """Delete the nth node (1-based index)"""
        if not self.head:
            raise IndexError("Cannot delete from an empty list.")

        if n <= 0:
            raise IndexError("Index must be a positive integer (1-based).")

        if n == 1:
            print(f"Deleting node at position {n} with value '{self.head.data}'")
            self.head = self.head.next
            return

        current = self.head
        prev = None
        count = 1

        while current and count < n:
            prev = current
            current = current.next
            count += 1

        if not current:
            raise IndexError(f"Index {n} is out of range.")

        print(f"Deleting node at position {n} with value '{current.data}'")
        prev.next = current.next

if __name__ == "__main__":
    ll = LinkedList()
    for value in [10, 20, 30, 40, 50]:
        ll.add_node(value)

    print("Initial linked list:")
    ll.print_list()

    try:
        ll.delete_nth_node(3)  
        print("\nAfter deleting 3rd node:")
        ll.print_list()
    except IndexError as e:
        print("Error:", e)

    try:
        ll.delete_nth_node(10)
    except IndexError as e:
        print("Error:", e)

    empty_list = LinkedList()
    try:
        empty_list.delete_nth_node(1)
    except IndexError as e:
        print("Error:", e)

