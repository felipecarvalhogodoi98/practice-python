from node import Node

class LinkedList(object):
  def __init__(self):
    self.head = None
    self.tail = None

  def set_head(self, node):
    self.head = node

  def set_tail(self, node):
    self.tail = node

  def __len__(self):
    node = self.head
    i = 0
    while node:
      node = node.get_next()
      i += 1
    return i
  
  def print_reverse(self):
    node = self.tail
    output = "{"
    while node:
      output += str(node.get_data()) 
      if node != self.head:
        output += " -> "
      node = node.get_prev()
    output += "}"
    print(output)
  
  def __str__(self):
    node = self.head
    output = "{"
    while node:
      output += str(node.get_data()) 
      if node != self.tail:
        output += " -> "
      node = node.get_next()
    output += "}"
    return output
  
  def push_front(self, data):
    node = Node(data)

    if self.head == None:
      self.head = node
      self.tail = node
    else:
      node.set_next(self.head)
      self.head.set_prev(node)
      self.head = node

  def push_back(self, data):
    node = Node(data)

    if self.head == None:
      self.head = node
      self.tail = node
    else:
      node.set_prev(self.tail)
      self.tail.set_next(node)
      self.tail = node

  def pop_front(self):
    node = self.head

    if self.head == self.tail and self.head != None:
      self.head = None
      self.tail = None
      return node.get_data()
    elif self.head:
      self.head = node.get_next()
      self.head.set_prev(None)
      return node.get_data()
    else:
      raise IndexError("Cannot pop on empty list.")
    
  def pop_back(self):
    node = self.tail

    if self.head == self.tail and self.head != None:
      self.head = None
      self.tail = None
      return node.get_data()
    elif self.tail:
      self.tail = node.get_prev()
      self.tail.set_next(None)
      return node.get_data()
    else:
      raise IndexError("Cannot pop on empty list.")

  def at(self, index):
    node = self.head
    i = 0

    while i != index and node:
      i += 1
      node = node.get_next()
    
    if i != index:
      raise IndexError("Index out of bounds.")
    
    return node.get_data()

  def delete(self, value):
    node = self.head

    while node:
      if (node.get_data() == value):
        prev = node.get_prev()
        next = node.get_next()

        if prev:
          prev.set_next(next)
        else:
          self.head = next
        if next:
          next.set_prev(prev)
        else:
          self.tail = prev
      node = node.get_next()

  def reverse(self):
    prev = None
    curr = self.head
    next = None

    self.tail = curr
    
    while curr:
      next = curr.get_next()
      curr.set_prev(next)
      curr.set_next(prev)

      prev = curr
      curr = next
    
    self.head = prev
