class Stack(object):
  def __init__(self):
    self.stack = []

  def __len__(self):
      return len(self.stack)
  
  def __str__(self):
    output = "["
    size = len(self.stack)

    for i in range(size):
      output += str(self.stack[i])
      if i + 1 != size:
        output += ", "

    output += "]"
    return output
  
  def push(self, item):
    self.stack.append(item)
  
  def pop(self):
    if (len(self.stack) > 0):
      return self.stack.pop()
