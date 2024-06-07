class Node(object):
  def __init__(self, data=None, next=None, prev=None):
    self.data = data
    self.next = next
    self.prev = prev
  
  def __str__(self):
    return str(self.data)

  def get_data(self):
    return self.data
  
  def get_next(self):
    return self.next
  
  def get_prev(self):
    return self.prev
  
  def set_data(self, data=None):
    self.data = data
  
  def set_next(self, next=None):
    self.next = next

  def set_prev(self, prev=None):
    self.prev = prev