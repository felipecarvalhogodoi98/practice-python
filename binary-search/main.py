import random

def binary_search(key, arr, min, max):
  if (max < min):
    return -1
  
  mid = int((min + max) // 2)

  if key > arr[mid]:
    return binary_search(key, arr, mid + 1, max)
  elif key < arr[mid]:
    return binary_search(key, arr, min, mid - 1)
  
  return mid

def generate_random_sorted_array():
  arr = []
  for i in range(10):
    arr.append(random.randint(0, 100))
  arr.sort()

  return arr

def test():
  arr = generate_random_sorted_array()
  
  for i in range(len(arr)):
    assert binary_search(arr[i], arr, 0, len(arr) - 1) == i

  assert binary_search(random.randint(101, 1000), arr, 0, len(arr) - 1) == -1
  assert binary_search(random.randint(101, 1000), arr, 0, len(arr) - 1) == -1
  assert binary_search(random.randint(101, 1000), arr, 0, len(arr) - 1) == -1
  
  print("all test ware successful.")

def main():
  test()
  
if __name__ == "__main__":
  main()