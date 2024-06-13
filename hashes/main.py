def word_in_file(file_name,  case_sensitive = False):
  words = {}

  with open(file_name) as file:
    for line in file:
      line = line.split()

      for word in line:
        if word:

          if not case_sensitive:
            word = word.lower() 

          if word in words: 
            words[word] += 1
          else:
            words[word] = 1

  return words
  
  return 0 

def main():
  words = word_in_file("big.txt", False)
  print(words)

  if "archive" in words:
    print(words["archive"])

if __name__ == "__main__":
  main()