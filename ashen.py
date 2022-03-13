
#Ashen Samarakkodige s4594169

print("Enter First Numbers List:")
fnumbers = input()
print("Enter Second Numbers List:")
snumbers = input()

a = fnumbers.split(" ")
b = snumbers.split(" ")
c =[]

for i in b:
  if i in a:
      c.append(i)

print("First Number Group 1: " + ' '.join(map(str,a)))
print("Second Number Group 2: " + ' '.join(map(str,b)))
print ("Resuts : "+ ' '.join(map(str,c)))