max = None
min = None

while True :
    x = input("Enter a number: ")
    if x == 'done':
        break
    try:
        ix = int(x)
    except:
        print('Invalid input')
        continue

    if max == None :
        max = ix
    if max < ix:
        max = ix

    if min == None :
        min = ix
    if min > ix :
        min = ix

print("Maximum is", max)
print("Minimum is", min)
