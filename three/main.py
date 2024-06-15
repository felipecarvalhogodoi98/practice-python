from binary_three import BinaryThree

def main():
  bt = BinaryThree()
  bt.insert(52)
  bt.insert(108)
  bt.insert(9)
  bt.insert(25)
  bt.insert(75)

  bt.in_order()

  bt.delete(52)

  # bt.in_order()

if __name__ == "__main__":
  main()