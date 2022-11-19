x = input("Enter max value : ")
x = int(x)
y = input("Enter O/E/B (Odd or Even or Both : ")
y = str(y)
z = input("Y/N (OnlyPrime?) : ")
z = str(z)

def check_even(x):
  if x > 2 and x % 2 == 0:
    prime = 1
    if prime == 1:
      for i in range(2, x):
        if x % i == 0:
          prime = 0
          break
    if prime == 1 and z == "N":
      print(x, "is prime number")
      x = check_even(x - 1)
    if prime == 0 and z == "N":
      print(x, "is not prime number")
      x = check_even(x - 1)
    if prime == 1 and z == "Y":
      print(x, "is prime number")
      x = check_even(x - 1)
    if prime == 0 and z == "Y":
      # print(x,"is not prime number")
      x = check_even(x - 1)
    return x
  if x > 2 and x % 2 == 1:
    x = check_even(x-1)
    return x
  if x < 2:
    return "Wrong input!!!"
  else:
    return '2 is prime number'

def check_odd(x):
  if x > 2 and x % 2 == 0:
    x = check_odd(x-1)
    return x
  if x > 2 and x % 2 == 1:
    prime = 1
    if prime == 1:
      for i in range(2, x):
        if x % i == 0:
          prime = 0
          break
    if prime == 1 and z == "N":
      print(x, "is prime number")
      x = check_odd(x - 1)
    if prime == 0 and z == "N":
      print(x, "is not prime number")
      x = check_odd(x - 1)
    if prime == 1 and z == "Y":
      print(x, "is prime number")
      x = check_odd(x - 1)
    if prime == 0 and z == "Y":
      # print(x,"is not prime number")
      x = check_odd(x - 1)
    return x
  if x < 1:
    return "Wrong input!!!"
  else:
    return '1 is prime number'

def check_both(x):
  if x > 1 :
    prime = 1
    if prime == 1 :
      for i in range(2,x):
        if x % i == 0:
          prime = 0
          break
    if prime == 1 and z == "N":
      print(x,"is prime number")
      x = check_both(x-1)
    if prime == 0 and z == "N":
      print(x,"is not prime number")
      x = check_both(x-1)
    if prime == 1 and z == "Y":
      print(x,"is prime number")
      x = check_both(x-1)
    if prime == 0 and z == "Y":
      #print(x,"is not prime number")
      x = check_both(x-1)
    return x

  if x < 1:
    return "Wrong input!!!"
  else:
    return '1 is prime number'

if y == "O":
  print(check_odd(x))
if y == "E":
  print(check_even(x))
if y == "B":
  print(check_both(x))