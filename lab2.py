# CS 2302 Data Structures: MW 1:30PM - 2:50PM
# Author: Stephanie Galvan
# Assignment: Lab 2 - Option B
# Instructor: Diego Aguirre
# TA: Gerardo Barraza
# Date of last modification: September 19, 2019
# Purpose: Given a file with unique and duplicate passwords, return a linked list
#          sorted with the 20 most common passwords (using bubble and merge sort)


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
        self.head = None
        self.tail = None
        self.length = 0

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


def get_llist(file):
    llist = LinkedList()
    # assume file already comes in the format of 'title.txt'
    with open(file) as f:
        for curr_line in f:
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


def check_duplicate(curr_node, llist):
    temp = llist.head
    not_in_list = True
    while temp:
        if curr_node.password == temp.password:
            temp.count += 1
            not_in_list = False
            return llist
        temp = temp.next
    # add passwords to the linked list and update tail every time
    if not_in_list:
        llist.tail.next = curr_node
        llist.tail = curr_node
        llist.length += 1
    return llist


def bubble_sort():
    print('Implement Bubble Sort')


def merge_sort():
    print('Implement Merge Sort')


def main():
    # for test purposes, the following file has 5 unique passwords and they repeat 4 times each
    test = get_llist("sameAmountOfDuplicates.txt")
    test.print_llist()
    # more files will be tested of course :)


main()
