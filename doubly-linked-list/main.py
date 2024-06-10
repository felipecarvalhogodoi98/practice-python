from list import LinkedList

def main():
  list = LinkedList()

  list.push_front(1)
  list.push_front(2)
  list.push_back(3)
  list.push_back(4)
  list.push_back(5)
  print(len(list))
  print(list)
  list.reverse()
  print(list)
  list.print_reverse()
main()