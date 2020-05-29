sumt = 0
lower = int(input("enter the lower bound of range"))
upper = int(input("enter the upper bound of range"))
for i in range(lower,upper + 1) :
    num = i
    while num != 0 :
        dig = num % 10
        sumt = sumt + dig ** 3
        num = num // 10
    if sumt == i :
        print(i)
    sumt = 0

