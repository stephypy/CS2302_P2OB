# CS 2302 Data Structures: MW 1:30PM - 2:50PM
# Author: Stephanie Galvan
# Assignment: Lab 2 - Option B
# Instructor: Diego Aguirre
# TA: Gerardo Barraza
# Date of last modification: September 24, 2019
# Purpose: Given a file with unique and duplicate passwords, return a linked list
#          sorted with the 20 most common passwords (using bubble and merge sort)

# Using pprint for the dictionary
import pprint
import time


class Node(object):
    password = ""
    count = -1
    next = None

    def __init__(self, password, count, next):
        self.password = password
        self.count = count
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None  # First node of linked list
        self.tail = None  # Last node of linked list
        self.length = 0

    # Print the entire linked list
    def print_llist(self):
        temp = self.head
        num = 0
        while temp:
            if num == 0:
                print('Head', num)
            else:
                print('Node ', num)
            print(' Password: ', temp.password, 'Count: ', temp.count, '\n')
            temp = temp.next
            num += 1

    # Print only the first 20 nodes
    def print_20(self):
        temp = self.head
        num = 0
        while num < 20:
            if num == 0:
                print('Head', num)
            else:
                print('Node ', num)
            print(' Password: ', temp.password, 'Count: ', temp.count, '\n')
            temp = temp.next
            num += 1


# This is Solution A for adding the passwords from the file on the linked list
def get_llist(file):
    llist = LinkedList()
    with open(file) as f:
        for curr_line in f:
            # Replacing the new line with a nothing
            curr_line = curr_line.replace('\n', '')
            # when linked list is empty, set the head and tail to the first line in file
            if not llist.head:
                llist.head = Node(curr_line, 1, None)
                llist.tail = llist.head
                llist.length += 1
            else:
                curr_node = Node(curr_line, 1, None)
                # traverse the linked list and increase count if duplicate
                llist = check_duplicate(curr_node, llist)
    return llist


# This is Solution B for adding passwords from the file to a dictionary
def get_dict(file):
    dict = {}
    # assume file already comes in the format of 'title.txt'
    with open(file) as f:
        for curr_line in f:
            curr_line = curr_line.replace('\n', '')
            if curr_line in dict:
                dict[curr_line] = dict[curr_line] + 1
            else:
                dict[curr_line] = 1
    return dict


# Helper function for get_llist; it will increase count if a duplicate is found
# else it will add the password to the list
def check_duplicate(curr_node, llist):
    temp = llist.head
    while temp:
        # increase count if a duplicate is found
        if curr_node.password == temp.password:
            temp.count += 1
            return llist
        temp = temp.next
    # add passwords to the linked list and update tail every time if its not in list
    llist.tail.next = curr_node
    llist.tail = curr_node
    llist.length += 1
    return llist


# descending order bubble sort
def bubble_sort(unsorted):
    # After the first iteration, the smallest count will be at the end
    # This is the last element we will check; it will get smaller
    last_element = None
    is_sorted = True

    # We will start with the maximum being the last node up until we reach a maximum of the first node
    while last_element is not unsorted.head:
        prev = None  # Keep variable for the previous node; prev will be initially zero since head has not previous
        first_node = unsorted.head  # Starting point

        # This is where we will be swapping nodes
        while first_node.next is not last_element:
            # Set the second node to be the node after the first one
            second_node = first_node.next

            # We will sort in descending order (5,4,3,2,1 ....)
            if first_node.count < second_node.count:
                is_sorted = False  # Since a swap happened, the linked list is still not sorted
                # Swapping:
                first_node.next = second_node.next
                second_node.next = first_node
                # After switching nodes, remember to connect previous node to the newly switched node
                if prev is not None:
                    # Update the prev node (it's the equal to the second node because a swap happened)
                    prev.next = second_node
                else:
                    # If a prev hadnt been set yet, then update head every time head is switched
                    unsorted.head = second_node

                # Update the first node and second note for the next iteration
                first_node, second_node = second_node, first_node

                # Update tail
                if second_node.next is None:
                    unsorted.tail = second_node

            # updating prev and first node (next iteration)
            prev = first_node
            first_node = first_node.next

        # Updating the last element
        last_element = first_node
        # This will prevent iterating several times if linked list is already sorted
        if is_sorted:
            break
    return unsorted


# Function 1 of merge sort
def merge_sort(start):
    # If theres only one head or if theres no head, just return the start
    if start is None or start.next is None:
        return start
    # split the linked list by left and right
    left, right = splitting(start)
    # Keep calling the merge sort (recursion) in order to keep splitting
    left = merge_sort(left)
    right = merge_sort(right)
    # Final answer will be the merging of the left and right side
    return merging(left, right)


# Function 2 of merge sort
def splitting(node):
    # Once theres no more nodes to be split (when the parameter is 1 or 0)
    if node is None or node.next is None:
        left = node
        right = None
        return left, right
    else:
        # obtaining the node for the right side
        mid = node
        temp = node.next
        while temp is not None:
            temp = temp.next
            if temp is not None:
                temp = temp.next
                mid = mid.next
    left = node
    right = mid.next
    mid.next = None
    return left, right


# Function 3 or merge sort
def merging(left, right):
    # A default node
    result = Node("", -1, None)
    curr = result
    while left and right:
        # Deciding in what order it should be sorted
        if left.count > right.count:
            curr.next = left
            left = left.next
        else:
            curr.next = right
            right = right.next
        curr = curr.next
    if left is None:
        curr.next = right
    if right is None:
        curr.next = left
    return result.next


# Function for verifying the creation of linked lists and dictionaries
def creating_list_tests(file):
    # Getting a linked list
    print('Linked List:')
    linked_list = get_llist(file)
    linked_list.print_llist()
    print('')

    # Getting a dictionary
    print('Dictionary:')
    diction = get_dict(file)
    pprint.pprint(diction)
    print('_________________')

    # Return the linked list we will be using to sort
    return linked_list


# Testing the sorting algorithms
def sorting_tests(linked_list):
    print('Bubble Sort:')
    start = time.time()
    bubble = bubble_sort(linked_list)
    end = time.time()
    print('Running time: ', end - start)
    if bubble.length >= 20:
        bubble.print_20()
    else:
        bubble.print_llist()

    print('')
    print('Merge Sort:')
    start = time.time()
    linked_list.head = merge_sort(linked_list.head)
    end = time.time()
    print('Running time: ', end - start)
    if linked_list.length >= 20:
        linked_list.print_20()
    else:
        linked_list.print_llist()


def main():
    # User will be prompted to choose one of the following options
    files = {1: '10-million-combos.txt', 2: '20unique.txt', 3: 'alreadySorted.txt', 4: 'ascendingOrder.txt',
             5: 'empty.txt', 6: 'sameAmountOfDuplicates.txt', 7: 'samePassword.txt', 8: 'smallTest.txt'}
    pprint.pprint(files)
    print('Please write the number of the file you want to test: \n')
    num = int(input())
    print('------------------------------')
    # First test: Getting linked lists vs dictionaries
    result = creating_list_tests(files[num])
    # Second test: Sorting algorithms (merge vs bubble)
    sorting_tests(result)


main()
