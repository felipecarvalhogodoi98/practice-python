from node import Node
from collections import deque

class BinaryThree(object):
  def __init__(self) -> None:
    self.root = None

  def insert(self, value):
    self.root = BinaryThree._insert(self.root, value)

  def search(self, value):
    node = BinaryThree._search(self.root, value)
    if node:
      return node.value

    return None 
  
  def delete(self, value):
    self.root = BinaryThree._delete_node(self.root, value)

  def level_order(self):
    if not self.root:
      return
    queue = deque([self.root])
    while queue:
      node = queue.popleft()

      print(node.value)

      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)

  def pre_order(self):
    BinaryThree._pre_order(self.root)

  def in_order(self):
    BinaryThree._in_order(self.root)

  def pos_order(self):
    BinaryThree._pos_order(self.root)

  @staticmethod
  def _delete_node(root, key):
      if root is None:
          return root
      if key < root.value:
          root.left = BinaryThree._delete_node(root.left, key)
      elif key > root.value:
          root.right = BinaryThree._delete_node(root.right, key)
      else:
          if root.left is None:
              return root.right
          elif root.right is None:
              return root.left
          temp = BinaryThree._min_value_node(root.right)
          root.value = temp.value
          root.right = BinaryThree._delete_node(root.right, temp.value)
      return root
  
  @staticmethod
  def _min_value_node(node):
      current = node
      while current.left is not None:
          current = current.left
      return current
  
  @staticmethod
  def _search(node, value):
      if node is None or node.value == value:
          return node
      if node.value < value:
          return BinaryThree._search(node.right, value)
      return BinaryThree._search(node.left, value)

  @staticmethod
  def _insert(node, value):
    if node is None:
      return Node(value)
    
    if node.value < value:
      node.right = BinaryThree._insert(node.right, value)

    if node.value > value:
      node.left = BinaryThree._insert(node.left, value)

    return node

  @staticmethod
  def _pre_order(node):
    if node:
      print(node.value)
      BinaryThree._pre_order(node.left)
      BinaryThree._pre_order(node.right)

  @staticmethod
  def _in_order(node):
    if node:
      BinaryThree._in_order(node.left)
      print(node.value)
      BinaryThree._in_order(node.right)
  
  @staticmethod
  def _pos_order(node):
    if node:
      BinaryThree._pos_order(node.left)
      BinaryThree._pos_order(node.right)
      print(node.value)

  