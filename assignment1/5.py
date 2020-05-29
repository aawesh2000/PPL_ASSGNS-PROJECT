
page = []
count = 0
flag = 0
print("enter the pages")
for i in range(25) :
    x = int(input())
    if x == -1 :
        break
    else :
        page.append(x)
        count += 1
print(page)
for i in range(1,26) :
    for j in range(count) :
        if page[j] == i :
            flag = 1
    if flag == 0 :
        print(i)
    flag = 0


