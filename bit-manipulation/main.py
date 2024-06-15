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

# round to power of 2
def round_power_2(x):
  x -= 1
  x |= x >> 1 # 2^1
  x |= x >> 2 # 2^2
  x |= x >> 3 # 2^3
  x |= x >> 4 # 2^4
  x |= x >> 5 # 2^5
  x += 1
  return x

def swap(obj):
  obj["a"] = obj["a"] ^ obj["b"]
  obj["b"] = obj["b"] ^ obj["a"]
  obj["a"] = obj["a"] ^ obj["b"]

def abs(x):
  _31bit = x >> 31
  return (x ^ _31bit) - _31bit

def main():
  # Even / Odd
  isEven = 1
  print(f'{isEven} is even: {is_even(isEven)}') # False
  
  # Count bits
  number1 = 0b110011
  number2 = 0b001100
  print(f'different bits [{number1}, {number2}]: {count_different_bits(number1, number2)}') # 6
  
  # Round power 2
  roundTo = 5
  print(f'round power {roundTo}: {round_power_2(roundTo)}')

  #Swap
  obj = {'a': 14, 'b': 25}
  print(f'Before swap a: {obj["a"]} ,b: {obj["b"]}')
  swap(obj)
  print(f'After swap a: {obj["a"]} ,b: {obj["b"]}')

  # Value abs
  numberNegative = - 5
  print(f'Before {numberNegative} -> After {abs(numberNegative)}')

if __name__ == "__main__":
  main()