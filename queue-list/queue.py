from collections import deque

class Queue(object):
  def __init__(self):
    self.queue = deque()

  def __str__(self):
    return str(self.queue).replace("deque", "queue")
  
  def __len__(self):
    return len(self.queue)
  
  def enqueue(self, item):
    self.queue.append(item)

  def dequeue(self):
    return self.queue.popleft()