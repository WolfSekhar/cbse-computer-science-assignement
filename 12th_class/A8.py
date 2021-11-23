# Write a Python program to implement a stack and queue using a list data-structure.

mylist = ["batman","robin","posidon"]
# Implementation for Stack
def size(list):
    return len(list)

def isEmpty(list):
    return size(list) == 0

def push(list,item):
    list.append(item)

def pop(list):
    if(not isEmpty(list)):
        list.pop(len(list) - 1)
def display(list):
    if(not isEmpty(list)):
        for i in list:
            print(i)
def top(list):
    if(not isEmpty(list)):
        return list[size(list) - 1]
print(top(mylist))

# Implementations for queue
def enqueue(list,item):
    list.append(item)

def dequeue(list):
    list.pop(0)

def isEmpty(list):
    return size(list) == 0
