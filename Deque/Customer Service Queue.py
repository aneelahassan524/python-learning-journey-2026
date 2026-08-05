from collections import deque

customers = [
    "Ali",
    "Sara",
    "Ahmed"
]
result = deque(customers)
print(f"Deque:{result}")
print(f"Initial Queue:{customers}")
result.appendleft("Aneela")
result.append("Bilal")
print(f"New Deque:{result}")
result.popleft()
result.pop()
print(f"Final Deque:{result}")