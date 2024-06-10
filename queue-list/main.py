from queue import Queue

def main():
  queue = Queue()

  print(queue)
  for i in range(10):
     queue.enqueue(i)
  print(queue)
  print(queue.dequeue())
  print(queue.dequeue())
  print(queue.dequeue())
  print(queue.dequeue())
  print(queue.dequeue())
  print(queue)
  queue.enqueue(20)
  print(queue)
  print(queue.dequeue())
  print(queue)
if __name__ == '__main__':
    main()