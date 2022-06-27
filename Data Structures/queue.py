from collections import deque
queue = deque([])

# append some value to queue
queue.append(1)
queue.append(2)
queue.append(3)

# FIFO - First In - First Out
queue.popleft()
print(queue)
if not queue:
    print("empty")  # Let the queue not empty
