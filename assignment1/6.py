sum1 = 0
sum2 = 0
for num1 in range(1,10000) :
    for k in range(1,num1) :
        if num1 % k == 0 :
            sum1 = sum1 + k

    num2 = sum1
    for i in range(1,num2) :
        if num2 % i == 0 :
            sum2 = sum2 + i
    if num1 != num2 and sum2 == num1 :
        print(num1,num2)
    sum1 = 0
    sum2 = 0

