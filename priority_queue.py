"""
Name: Ashwin Gowda  asg7954@rit.edu
File: asg7954@rit.edu
Purpose: To change regular queue immutable queue to priority queue
"""
from node import *
from dataclasses import dataclass
from typing import Any, Union

# Makes the dataclass
@dataclass
class PriorityQueue:
    size: int
    front: Union[None, Node]
    back: Union[None, Node]




def make_priority_queue():
    """
    Makes an empty PriorityQueue
    :return: an empty priority queue
    """
    return PriorityQueue(0, None, None)



def enqueue(queue, element):
    """
    Insert an element into the back of the queue. (Returns None)
    """
    newnode = Node(element, None)
    if is_empty(queue):
        queue.front = newnode
    elif element.priority >= queue.back.value.priority:
        queue.back.rest = newnode
    else:
        if element.priority <= queue.front.value.priority and element.priority >= queue.front.rest.priority:
            queue.front.rest = newnode
        else:
            enqueue(queue.rest, element)

    queue.back = newnode
    queue.size = queue.size + 1


def dequeue(queue):
    """
    Remove the front element from the queue. (returns removed value)
    precondition: queue is not empty.
    """
    if is_empty(queue):
        raise IndexError("dequeue on empty queue")
    removed = queue.front.value
    queue.front = queue.front.rest
    if is_empty(queue):
        queue.back = None
    queue.size = queue.size - 1
    return removed


def front(queue):
    """
    Access and return the first element in the queue without removing it.
    precondition: queue is not empty.
    """
    if is_empty(queue):
        raise IndexError("front on empty queue")
    return queue.front.value


def back(queue):
    """
    Access and return the last element in the queue without removing it
    precondition: queue is not empty.
    """
    if is_empty(queue):
        raise IndexError("back on empty queue")
    return queue.back.value


def is_empty(queue):
    """
    Is the queue empty?
    """
    return queue.front == None