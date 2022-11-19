x = eval(input("Enter height of diamond:"))
def Diamond(x):
    for i in range(x):
        print(" " * (x-i),"X" * (2*i + 1))

    for i in range( x- 2, -1, -1):
        print(" " * (x - i),"X"*(2*i+1))

ip = int(input("enter the Diamonds length : "))

for i in range(0,ip):
    Diamond(x)