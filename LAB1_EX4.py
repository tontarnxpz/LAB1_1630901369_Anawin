limit = int(input("Input Limit : "))
value_new = 0
for i in range(0,limit):
   value_old = 1/(i+1)
   value_new = value_old+value_new

print("Harmonic step =",limit)
print(value_new)