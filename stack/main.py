from stack import Stack

def main():
  stack = Stack()

  print(stack)
  print(len(stack))
  stack.push(1)
  stack.push(2)
  stack.push(3)
  print(stack)
  print(stack.pop())
  print(len(stack))

main()