#Implement an algorithm to determine if a string has all unique characters


tablesize = 128
mytable = [[] for _ in range(tablesize)]

def hasher(string):
  total = 0
  for letter in string:
    total += ord(letter)
  return total % tablesize

def insert(table, string):
  for letter in string:
    key = hasher(letter)
    table[key].append(letter)
    if len(table[key]) > 1:
      print("duplicate %s" % letter)
      return False

