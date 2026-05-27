class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __len__(self):
        count = 0
        current_node = self.head

        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count

    def add_node(self, value):
        new_node = ListNode(value)

        if self.head is None:
            self.head = new_node
            return
            
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def remove_last(self):

        if self.head is None:
            print("List is Empty")
            return
        
        if self.head.next is None:
            self.head = None
            return
        
        previous_node = None
        current_node = self.head

        while current_node.next is not None:
            previous_node = current_node
            current_node = current_node.next

        previous_node.next = None

    def remove_by_value(self, value):
        current_node = self.head
        previous_node = None

        #remove head
        if current_node is not None and current_node.value == value:
            self.head = current_node.next
            return
        
        while current_node is not None and current_node.value != value:
            previous_node = current_node
            current_node = current_node.next
        
        #value not found
        if current_node is None:
            return
        
        previous_node.next = current_node.next
    
    def insert_at_head(self, value):
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_position(self, value, position):
        new_node = ListNode(value)

        if position < 0:
            print("Invalid position")
            return
        
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current_node = self.head
        previous_node = None
        current_position = 0

        while current_node is not None and current_position < position:
            previous_node = current_node
            current_node = current_node.next
            current_position +=1

        if current_node is None:
            print("Position Not Found so add in End of List")
            previous_node.next = new_node
            return
        
        new_node.next = current_node
        previous_node.next = new_node

    def sum_of_list(self):
        total_sum = 0
        current_node = self.head

        while current_node is not None:
            total_sum += current_node.value
            current_node = current_node.next
        return total_sum
    
    def reverse_list(self):
        previous_node = None
        current_node = self.head

        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node

    def print_list(self):
        print("\n")
        current_node = self.head

        while current_node is not None:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")

list = LinkedList()

while True:
    print("\n_______________Link List Operation_______________\n")
    print("1. Append Node")
    print("2. Remove Last Node")
    print("3. Remove Node by Value")
    print("4. Enter Node at Head ")
    print("5. Enter Node At Specific position")
    print("6. Get Sum of List")
    print("7. Reverse Current List")
    print("8. Exit \n")
    print(f"Current Link List \t current length of list-{len(list)}")
    list.print_list()

    choice = int(input("\nEnter Your Choice : "))
    
    match choice:

        case 1:
            value = int(input("Enter Value To Append : "))
            list.add_node(value)

        case 2:
            list.remove_last()

        case 3:
            value = int(input("Enter Value of Node to Remove node : "))
            list.remove_by_value(value)
        
        case 4:
            value = int(input("Enter Value To Add at Head : "))
            list.insert_at_head(value)

        case 5:
            value = int(input("Enter Value : "))
            position = int(input(f"On which position you want to add {value} : "))
            list.insert_at_position(value, position)
        
        case 6:
            print(list.sum_of_list())

        case 7:
            print(list.reverse_list())

        case 8:
            print("\nExiting....\n")
            break

        case _:
            print("Please Enter Valid Choice")
