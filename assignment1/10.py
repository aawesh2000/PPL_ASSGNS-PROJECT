a = int(input("enter first term\n"))
r = int(input("enter common difference\n"))
for i in range(1,11):
    term = a * (r ** (i - 1))
    print(term)
