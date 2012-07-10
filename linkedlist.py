#! /opt/local/bin/python

import sys

class Node():
	value = ""
	next = None

	def __init__(self, value="", next=None):
		self.value = value
		self.next = next


head = None

def initialize(count=10):
	current = Node(0)
	head = current
	for i in range(1,count+1):
		new = Node(i)
		current.next = new
		current = new

	return head

def print_list(head):
	current = head
	while True:
		print current.value
		current = current.next
		if current is None:
			break


def reverse(head):
	prev = None
	current = head
	while (current is not None):
		next = current.next
		current.next = prev
		prev = current
		current = next
	return prev


def reverse_recursive(current, prev=None):
	if current is None:
		return prev
	last = reverse_recursive(current.next, current)
	current.next = prev
	return last


def append_node(current, new_node):
	head = current
	while current.next is not None:
		current = current.next
	current.next = new_node
	return head


def prepend_node(current, new_node):
	new_node.next = current
	return new_node


def nth_last(head, n):
    current = nth = prev = head
    offset = 0
    while current is not None:
        if offset <= n:
            offset += 1
        else:
            nth = nth.next
        prev = current
        current = current.next
    if offset < n:
        return prev
    else:
        return nth


if __name__ == "__main__":

	# Initialize the linkedlist
	head = initialize(8)


	operation = raw_input("Which operation would you like to perform:\n"\
				"A) Reverse\n"\
				"B) Reverse\n"\
				"C) Append Node\n"\
				"D) Prepend Node\n"\
                "E) Nth to last Node\n"\
				"> ")
	if operation.lower() == 'a':
		head = reverse(head)
		print_list(head)
	elif operation.lower() == 'b':
		head = reverse_recursive(head)
		print_list(head)
	elif operation.lower() == 'c':
		head = append_node(head, Node('new'))
		print_list(head)
	elif operation.lower() == 'd':
		head = prepend_node(head, Node('new'))
		print_list(head)
	elif operation.lower() == 'e':
		node = nth_last(head, 4)
		print node.value