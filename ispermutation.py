# Given two strings write a method to decide if one is a permuatation of the other.

def ispermutation(string1, string2):

  if len(string1) != len(string2):
    print("cannot be permutation")
    return False

  l1 = list(string1)
  l2 = list(string2)
  l1.sort()
  l2.sort()

  if l1 == l2:
    print("they are permutations")
    return True

  if l1 != l2:
    print("not permutation")
    return False

ispermutation('dog', 'god')