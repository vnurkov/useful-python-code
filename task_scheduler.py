from generator import countdown
from collections import deque


tasks = deque()
tasks.extend([countdown(10), countdown(5), countdown(15)])

def run():
    while tasks:
        task = tasks.popleft()
        try:
            x = next(task)
            print(x)
            tasks.append(task)
        except StopIteration:
            print("Task Fished")
