"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
       self.value = value
       self.prev = prev
       self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 0 if node is None else 1

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        #create a new_node
        new_node = ListNode(value)
        self.length += 1        
        # add to empty list
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # add to non-empty list
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        #save the value of the current head
        value = self.head.value
        #removes current head 
        self.delete(self.head)
        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length +=1
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        value = node.value
        if node is self.head:
            return None
        if node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1
        self.add_to_head(value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return

        value = node.value

        if node is self.head:
            self.remove_from_head()
            self.add_to_tail(value)
        else:
            node.delete()
            self.length -= 1
            self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        #dont need to return value        
        #Do need to update Head, Tail
        if not self.head:
            return None

        self.length -= 1

        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif node is self.head: #list has 2+ nodes
            self.head = node.next
            node.delete()
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        #If length is 0 return None
        if self.length == 0:
            return None
        #If length is 1 return self.head.value
        if self.length == 1:
            return self.head.value
        #Current_max starts as self.head.value
        current_max = self.head.value
        #Iterate through the list
        current_node = self.head
        #Stop when current_node is None
        while current_node is not None:
        #Compare current_max to each value and update current_max if value > current_max
            if current_max < current_node.value:
                current_max = current_node.value
        #Move current_node forward
            current_node = current_node.next
        #Return current_max
        return current_max