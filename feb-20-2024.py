# Good morning! Here's your coding interview problem for today.
# This problem was asked by Google.
# Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
# In this example, assume nodes with the same value are the exact same node objects.
# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def create_intersecting_lists(list1_length, list2_length, intersection_point):
    # Create the first linked list
    head1 = ListNode(1)
    current1 = head1
    for i in range(2, list1_length + 1):
        new_node = ListNode(i)
        current1.next = new_node
        current1 = new_node
    
    # Create the second linked list
    head2 = ListNode('a')
    current2 = head2
    for i in range(2, list2_length + 1):
        new_node = ListNode(chr(ord('a') + i - 1))
        current2.next = new_node
        current2 = new_node
    
    # Make the lists intersect at the specified intersection point
    temp = head1
    for _ in range(intersection_point - 1):
        temp = temp.next
    current2.next = temp

    return head1, head2

# Example usage:
list1_length = 5
list2_length = 7
intersection_point = 3
head1, head2 = create_intersecting_lists(list1_length, list2_length, intersection_point)

# Print the linked lists
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("Nonel")

def solve(head1, head2):
    addresses = set()
    while head1 != None:
        addresses.add(head1)
        head1 = head1.next
    
    while head2 != None:
        if head2 in addresses:
            return head2

        head2 = head2.next
    
    return 'No intersection'

def find_intersection(list_a, list_b):
    if not list_a or not list_b:
        return None

    pointer_a = list_a
    pointer_b = list_b

    while pointer_a != pointer_b:
        print('comparison', (pointer_a.value if pointer_a != None else None) , (pointer_b.value if pointer_b != None else None))
        pointer_a = pointer_a.next if pointer_a else list_b
        pointer_b = pointer_b.next if pointer_b else list_a

    return pointer_a


print("Linked List 1:")
print_linked_list(head1)

print("\nLinked List 2:")
print_linked_list(head2)

print_linked_list(find_intersection(head1, head2))
