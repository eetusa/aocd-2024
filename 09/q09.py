from __future__ import annotations
from aocd import data
from typing import Optional

example0 = "12345"
example = "2333133121414131402"

class Node:
    id: int
    position: int
    empty_space: bool
    next: Node | None
    previous: Node | None

    def __init__(self, id: int, position: int, empty_space: bool, next: Optional[Node] = None, previous: Optional[Node] = None):
        self.id = id
        self.position = position
        self.next = next
        self.previous = previous
        self.empty_space = empty_space

    def __str__(self):
        return f'Node(ID: {self.id}, Position: {self.position}, Empty Space: {self.empty_space})'

    def __repr__(self):
        return f'Node(ID: {self.id}, Position: {self.position}, Empty Space: {self.empty_space}, Next: {self.next}, Previous: {self.previous})'

class DoublyLinkedList:
    def __init__(self):
        print("Initializing list")
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def append(self, id: int, empty_space: bool):
        position = 0
        if self.head:
            position = self.tail.position + 1

        new_node = Node(id, position, empty_space)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.previous = self.tail
        self.tail = new_node

    def remove(self, node: Node):
        if node.previous:
            node.previous.next = node.next
        if node.next:
            node.next.previous = node.previous
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.previous
        node.next = node.previous = None

    def set_to_empty(self, node: Node):
        node.id = -1
        node.empty_space = True

    def get_first(self) -> Node:
        return self.head
    
    def get_last(self) -> Node:
        return self.tail
    
    def get_tail_pointer_size(self, tail_pointer: Node) -> int:
        pointer_id = tail_pointer.id
        size = 1
        current = tail_pointer

        while(True):
            if not current.previous:
                break
            if current.previous.id == pointer_id:
                size = size + 1
                current = current.previous
            else:
                break
        return size
    
    def get_empty_pointer_size(self, empty_pointer: Node) -> int:
        size = 1
        current = empty_pointer

        while(True):
            if not current.next:
                break
            if current.next.empty_space:
                size = size + 1
                current = current.next
            else:
                break
        return size
    
    def move_tail_pointer_to_previous(self, tail_pointer: Node) -> Node:
        current = tail_pointer
        start_id = current.id

        while(True):
            if not current.previous:
                return None
            if current.id == -1:
                current = current.previous
                continue
            if current.id == start_id:
                current = current.previous
                continue
            return current

    def move_current_pointer_to_next_non_empty(self, current_pointer: Node) -> Node:
        current = current_pointer

        if not current.empty_space:
            return current

        while(True):
            if not current.next:
                return None
            if not current.next.empty_space:
                return current.previous
            
    def print_list_forward(self):
        current = self.head
        while current:
            if current.empty_space:
                print(".", end="")
            else:
                print(current.id, end="")
            current = current.next
        print()

    def print_checksum(self):
        checksum = 0
        current = self.head
        while current:
            if not current.empty_space:
                checksum = checksum + (current.position * current.id)
            current = current.next
        print(f'Checksum: {checksum}')

def parse_input(input: str) -> list[int]:
    result: list[int] = []

    for c in input:
        result.append(int(c))
    return result

def add_value_to_list(linked_list: DoublyLinkedList, value: int, index: int):
    id = -1

    if index % 2 == 0:
        id = index // 2

    is_empty: bool = index % 2 != 0
    for i in range(0, value):
        linked_list.append(id, is_empty)

def optimize_list(linked_list: DoublyLinkedList):
    current = linked_list.get_first()
    tail = linked_list.get_last()

    while(True):
        previous = current.previous
        next = current.next
 
        if (current == tail):
            return
        if (current.next == None):
            return
        while(tail.empty_space):
            tail = tail.previous
        if (current.empty_space):
            current = Node(tail.id, current.position, False, current.next, current.previous)
            if previous:
                previous.next = current
            if next:
                next.previous = current
            linked_list.set_to_empty(tail)
            linked_list.tail = tail.previous
            tail = linked_list.tail

        current = current.next

def optimize_list_whole_blocks(linked_list: DoublyLinkedList):
    current = linked_list.get_first()
    tail = linked_list.get_last()
    last_position = tail.position
    linked_list.print_list_forward()

    if (tail.empty_space):
        while(tail.empty_space):
            tail = tail.previous
    tail_size = linked_list.get_tail_pointer_size(tail)


    while(True):
        if current.position >= tail.position:
            break
        if tail.position % 100 == 0:
            print(f'{tail.position} / {last_position}')

        if (current.empty_space):
            empty_space_size = linked_list.get_empty_pointer_size(current)

            if (empty_space_size >= tail_size):
                for i in range(0, tail_size):
                    previous = current.previous
                    next = current.next

                    if not current.next:
                        break
                    current = Node(tail.id, current.position, False, current.next, current.previous)

                    if previous:
                        previous.next = current
                    if next:
                        next.previous = current

                    tail.id = -1
                    tail.empty_space = True

                    if not tail.previous:
                        print("huh?")
                        break

                    tail = tail.previous
                    current = current.next
                current = linked_list.head
                while(tail.empty_space):
                    tail = tail.previous
                tail_size = linked_list.get_tail_pointer_size(tail)
            else:
                if (current.next == tail):
                    tail = linked_list.move_tail_pointer_to_previous(tail)
                    if tail == None:
                        return
                    tail_size = linked_list.get_tail_pointer_size(tail)
                    current = linked_list.head
                else:
                    current = current.next
                
        else:
            if (current.next == tail):
                tail = linked_list.move_tail_pointer_to_previous(tail)
                if tail == None:
                    return
                tail_size = linked_list.get_tail_pointer_size(tail)
                current = linked_list.head
            else:
                current = current.next

# Seems that I somehow broke a while doing b, but _should_ now be fixed
def solve_a(input: str):
    linked_list = DoublyLinkedList()
    parsed_input = parse_input(input)
    for index, value in enumerate(parsed_input):
        add_value_to_list(linked_list, value, index)

    optimize_list(linked_list)
    linked_list.print_list_forward()
    linked_list.print_checksum()

def solve_b(input: str):
    linked_list = DoublyLinkedList()
    parsed_input = parse_input(input)
    for index, value in enumerate(parsed_input):
        add_value_to_list(linked_list, value, index)

    optimize_list_whole_blocks(linked_list)
    linked_list.print_checksum()

# Note: this doubly linked list solution definitely wasn't worth it for B side -- runtime nearly 5 minutes
solve_a(data)
solve_b(example)