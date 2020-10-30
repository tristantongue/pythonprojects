for fizzbuzz in range(50):
  if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
    print('fizzbuzz')
    continue
  if fizzbuzz % 3 == 0:
    print('fizz')
    continue
  if fizzbuzz % 5 == 0:
    print('buzz')
    continue
  print(fizzbuzz)