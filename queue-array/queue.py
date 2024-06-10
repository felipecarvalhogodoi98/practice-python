class Queue(object):
  def __init__(self, capacity) -> None:
    self.head = 0
    self.tail = 0
    self.capacity = capacity + 1
    self.queue = []

  def __str__(self):
    return "queue(" + str(self.queue) + ")"
  
  def full(self):
    return (self.tail + 1) % self.capacity == self.head
  
  def empty(self):
    return self.head == self.tail

  def enqueue(self, item):
    if (self.full()):
      print("Cannot enqueue from full queue.")
      exit()
    
    self.queue.append(item)
    self.tail = (self.tail + 1) % self.capacity

  def dequeue(self):
    if (self.empty()):
      print("Cannot dequeue from empty queue.")
      exit()
      
    self.head = (self.head + 1) % self.capacity
    return self.queue.pop(0)