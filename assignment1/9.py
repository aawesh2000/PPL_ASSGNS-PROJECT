sumt = 0
count = 0
for i in range(1,10000) :
    for j in range(1,i + 1) :
        if i % j == 0 :
            sumt = sumt + (1/j)
            count += 1
    if sumt != 0 :
        hm = count / sumt
        if (hm % 1 < 0.00006 and hm % 1 >= 0 ) or (hm % 1 < 1 and hm % 1 > 0.99996):
            print(i)
    sumt = 0
    count = 0
