def set_bit(x, position):
  mask = 1 << position
  return x | mask

def clear_bit(x, position):
  mask = 1 << position
  return x & ~mask

def flip_bit(x, position):
  mask = 1 << position
  return x ^ mask

def is_bit_set(x, position):
  shifted = x >> position
  return shifted & 1

def is_even(x):
  return (x & 1) == 0

def is_power_two(x):
  return (x & x-1) == 0

# How many bits are different between two numbers
def count_different_bits(x, y):
  xorded = bin(x ^ y)
  return xorded.count("1")

def main():
  print(is_even(1)) # False
  print(count_different_bits(0b110011, 0b001100)) # 6


if __name__ == "__main__":
  main()