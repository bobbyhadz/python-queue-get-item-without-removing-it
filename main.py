# Get an item from a Queue in Python without removing it

import queue

q = queue.Queue()

for item in range(10):
    q.put(item)


print(q.queue[0])  # 👉️ 0
print(q.queue[0])  # 👉️ 0

print(q.queue[1])  # 👉️ 1