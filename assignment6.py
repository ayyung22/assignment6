#CIS 103 XY Fundamentals of Programming
#Homework Assignment: Arrays and Linked Structures
#Author: Annie Yung
#Date: 11/2/2024

print("Part 1: Array Implementation and Operations")
class Array:

    def __init__(self, capacity, fill_value=None):
        """Initialize an array with a fixed capacity and optional fill value."""
        self.items = [fill_value] * capacity

    def __len__(self):
        """Return the length of the array."""
        return len(self.items)

    def __str__(self):
        """Return a string representation of the array."""
        return str(self.items)

    def __getitem__(self, index):
        """Get an item at a specific index."""
        return self.items[index]

    def __setitem__(self, index, value):
        """Set an item at a specific index."""
        self.items[index] = value

#Testing the Array class#
array = Array(10, fill_value=0)  # Create an array of size 10, filled with 0
print("Initial array:", array)
array[2] = 4 #Setting the third element to 4
print("Modified array", array)
array[3] = 3 #Setting the fourth element to 3
print("Modified array", array)
print("Access element is: ", array[2])

print()
print()

print("Part 1: Array Resizing")


class Array:
    def __init__(self, initial_capacity=4):
        self.size = 0  # Current number of elements
        self.capacity = initial_capacity  # Initial capacity
        self.array = [None] * self.capacity

    def __resize_up(self):
        #This will double the capacity of the array
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity
        print(f"Array increased up to {self.capacity}")

    def __resize_down(self):
        # Half the capacity of the array
        new_capacity = max(self.capacity // 2, 4)
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity
        print(f"Array decreased down to {self.capacity}")

    def add(self, value):
        # If the array is full, resize up
        if self.size == self.capacity:
            self.__resize_up()

        self.array[self.size] = value
        self.size += 1

    def remove(self, value):
        # Find the index of the value to remove
        for i in range(self.size):
            if self.array[i] == value:
                # Shift elements left to remove the value
                for j in range(i, self.size - 1):
                    self.array[j] = self.array[j + 1]
                self.array[self.size - 1] = None  # Clear the last element
                self.size -= 1

                # If the array is less than half full, it will resize down
                if self.size <= self.capacity // 4:
                    self.__resize_down()

                return
        print(f"{value} not found in array.")

    def get(self, index):
        # Get the element at the given index
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds.")
        return self.array[index]

# Example Usage:
arr = Array(4)

# Add elements
arr.add(0)
arr.add(5)
arr.add(10)
arr.add(15)
print(arr)

arr.add(20)  # Triggers resize up
print(arr)

# Remove elements
arr.remove(0)
print(arr)

arr.remove(5)
arr.remove(10)  # Triggers resize down
print(arr)

print()
print()

print("Part 1: Basic Operations")


class Array:
    def __init__(self, initial_capacity=4):
        self.size = 0  # Current number of elements
        self.capacity = initial_capacity  # Initial capacity
        self.array = [None] * self.capacity  # Internal array to hold elements

    def __resize_up(self):
        # Double the capacity of the array
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity
        print(f"Array increased up to {self.capacity}")

    def __resize_down(self):
        # Half the capacity of the array
        new_capacity = max(self.capacity // 2, 4)
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity
        print(f"Array decreased down to {self.capacity}")

    def add(self, value):
        # If the array is full, resize up
        if self.size == self.capacity:
            self.__resize_up()

        self.array[self.size] = value
        self.size += 1

    def remove(self, value):
        #This will find the index of the value to remove
        for i in range(self.size):
            if self.array[i] == value:
                for j in range(i, self.size - 1):
                    self.array[j] = self.array[j + 1]
                self.array[self.size - 1] = None
                self.size -= 1

                # If the array is less than half full, resize down
                if self.size <= self.capacity // 4:
                    self.__resize_down()

                return
        print(f"{value} not found in array.")

    def get(self, index):
        # Get the element at the given index
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds.")
        return self.array[index]

    def set(self, index, value):
        # Set the value at the given index
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds.")
        self.array[index] = value

    def __str__(self):
        # Return a string representation of the array
        return f"[{', '.join(str(self.array[i]) for i in range(self.size))}]"


# Create an array with a capacity of 5
arr = Array(5)

# Populate the array with values
arr.add(0)
arr.add(5)
arr.add(10)
arr.add(15)
arr.add(20)

# Display the array
print("Array:", arr)

# Access elements by index
print("Element at the chosen index:", arr.get(2))

# Modify an element at a specific index
arr.set(2, 100)

# Display the array after modification
print("Array after modifying index 2:", arr)

print()
print()

print("Part 1: Physical vs Logical Size")
def check_and_resize_array(arr):
    # Logical size (number of elements in the array)
    logical_size = len(arr)

    physical_size = len(arr)

    #Check if logical size equals physical size
    if logical_size == physical_size:
        print("Logical size equals physical size. Increasing capacity to...")

        # Increase capacity by doubling the array size
        arr.extend([None] * logical_size)
        print("New logical size:", len(arr))
        print("Array after resizing:", arr)
    else:
        print("No resizing is needed. The logical size is less than physical size.")


# Example
arr = [0, 1, 2]  # Initial array with 3 elements

check_and_resize_array(arr)

print()
print()

print("Part 2: Linked Structure Implementation")
class Node:
    def __init__(self, data):
        #Initializing a new node with data and next pointer
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None  #Empty list
        self.size = 0

def insert_at_beginning(head, data):
    # Inserting a new node at the beginning of the linked list
    new_node = Node(data)
    new_node.next = head
    return new_node

def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:
        return new_node

    current = head
    while current.next:
        current = current.next

    current.next = new_node
    return head

def delete_at_beginning(head):
    if head is None:
        print("Error: Singly linked list is empty")
        return None

    new_head = head.next
    del head
    return new_head

def search(head, data):
    current = head
    while current:
        if current.data == data:
            return True
        current = current.next
        return False

def traverse(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


#Example
head = None
head = insert_at_beginning(head, 3)
head = insert_at_beginning(head, 2)
head = insert_at_beginning(head, 1)
head = insert_at_beginning(head, 0)

insert_at_end(head, 4)

# Deleting the node at the beginning
head = delete_at_beginning(head)

# Traversing and print the nodes after deletion
traverse(head)

print()
print()

print("Part 3: Code Experimentation")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Creating class LinkedList
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Function to demonstrate both array and linked list usage
def main():
    # Using an array (list in Python)
    array_numbers = [0, 5, 10, 15, 20]

    print("Array:")
    for num in array_numbers:
        print(num, end=" ")
    print("\n")

    # Using a linked list
    linked_list = LinkedList()
    for num in array_numbers:
        linked_list.append(num)

    print("Linked List:")
    linked_list.print_list()


# Run the program
if __name__ == "__main__":
    main()
