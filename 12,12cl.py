class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.value

    def update(self, value):
        '''Updates value of the Node object'''
        super().__init__(value)

class LinkedList:

    def __init__(self):
        self.head = None

    def __iter__(self):
        current_item = iter(self.head)
        return current_item

    def __next__(self):
        current_item = self.head
        if current_item is not None:
            val = current_item.value
            current_item = current_item.next
            return val
        else:
            raise StopIteration

    def __len__(self):
        '''Returns number of Nodes in the list.
        When this method defined, built-in len function can be called on class instances
        '''
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count

    def add_to_tail(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def add_to_head(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node

    def is_empty(self):
        '''Returns True if there no Nodes in the list, False otherwise'''
        return self.head.next is None

    def pop(self):
        '''Removes last Node from the list and returns it'''
        if self.is_empty():
            raise Exception('Stack is empty')
        answer = self.head.value
        self.head = self.head.next
        self.__len__ -= 1
        return answer

    def copy(self):
        '''Returns a copy of linked list. Any changes of copy would not affect
        original list
        '''
        result = list()
        current = self.head
        while current.next != None:
            result.add_to_tail(current,value)
            current = current.next
        result.add_to_tail(current,value)
        return result

    def sorted(self):
        '''Returns a copy of linked list, sorted in ascending order -
        Node with smallest value goes first. Original list will not be
        changed by this method
        '''
        sorted_list = self.copy()
        if sorted_list.is_empty == True:
            print('List is empty!')
        else:
            for index in range(0, sorted_list.__len__()):
                current = sorted_list.head
                index += 1
                while current.next is not None:
                    if current.value > current.next.value:
                        tmp = current
                        next_tmp = current.next.next
                        current = current.next
                        if tmp != sorted_list.head:
                            current.next = tmp
                            current.next.next = next_tmp
                index += 1
        return sorted_list


    def reversed(self):
        '''Returns a copy of the linked list where Nodes are oredered in reverse order:
        head node of original list becomes a tail for copy
        '''
        reversed_list = self.copy()
        previous = None
        current_node = self.head
        while current_node:
            temp = current_node.next
            current_node.next = previous
            previous = current_node
            current_node = temp
            self.head = previous
        return reversed_list

    def is_palindrome(self,value,palindrom):
        '''A palindrome is a sequence that reads the same forward and backward.
        Method returns True if current list is a palindorome, False otherwise
        '''
        node = Node(value)
        start = palindrom.head
        end = palindrom.node
        while start != end and end.next != start:
            if start.value != end.value:
                return False
            start = start.next
            end = palindrom.add_to_tail(end)
        return True


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.add_to_tail(1)
    linked_list.add_to_tail(2)
    linked_list.add_to_tail(5)
    linked_list.add_to_tail(10)
    for node in linked_list:
        print(node)

    assert len(linked_list) == 4
    assert linked_list.is_empty() == False
    assert linked_list.pop().value == 2
    list_copy = linked_list.copy()
    list_copy.add_to_tail(12)
    assert len(list_copy) != len(linked_list)
    sorted_copy = linked_list.sorted()
    assert linked_list.is_palindrome() == False
    assert linked_list.reversed().head.value == 1