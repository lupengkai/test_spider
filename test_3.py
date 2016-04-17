from collections import deque

queue  = deque(['Erric', 'John', 'Michael'])

queue.append('Terry')
queue.append('Graham')

print(queue.popleft())
print(queue.popleft())
print(queue)