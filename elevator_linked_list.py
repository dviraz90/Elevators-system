class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
    
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    

    def move_to_end(self, head_ref) :
    
        if head_ref == None or head_ref.next == None:
            return None
    
        first = head_ref
        last = head_ref
        while last.next is not None:
            last = last.next
        
        head_ref = first.next
        first.next = None
        last.next = first
        return head_ref

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

