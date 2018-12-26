"""
Name: Ashwin Gowda    asg7954@rit.edu
File: tasks.py
Purpose: Used as a task file to
"""
from priority_queue import *
from dataclasses import dataclass

@dataclass
class Task:
    name: str
    priority: int

def make_task(name, priority):
    """
    Makes an empty task
    :param name: What the name of the task is
    :param priority: How high the priority is
    :return: An empty task
    """
    return Task(name, priority)


def main():
    q = make_priority_queue()
    task2 = Task("Task2", 4)
    task3 = Task("Task3", 5)
    task4 = Task("Task4", 8)

    enqueue(q, task2)
    enqueue(q, task3)
    enqueue(q, task4)
    print(q)


main()


