# Given a string, write a function to check if it is a permutation foa palindrome

tablesize = 128
mytable = [[] for _ in range(tablesize)]

def hasher(string):
  total = 0
  for letter in string:
    total += ord(letter)
  return total % 128

def ispalindrome(table, string):
  for letter in string:
    key = hasher(letter)
    table[key].append(letter)
  oddcount = 0
  for element in table:
    if len(element) % 2 == 1:
      oddcount += 1
  if oddcount > 1 :
    print("not a palindrome")
    return False
  print('is a palindrome')
  return True
