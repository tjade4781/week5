num = 0
sum = 0.0
while True :
    x = input('Enter Number:')
    if x == 'done' :
        break
    try:
        fval = float(x)
    except:
        print ('Invalid Input')
        continue
    num= num + 1
    sum = sum + fval

print(sum, num, sum/num)
