for letter in 'python':
    print('Current Letter :', letter)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
  if (fruit == 'apple'):
    print("Apple")
  else:
    print("current fruit is", fruit)


for letter in 'Python':
  if letter == 'o':
    break
  elif letter == 't':
    continue
  elif letter == 'y':
    pass
    print('This is pass block')
  print('Current Letter :', letter)
  