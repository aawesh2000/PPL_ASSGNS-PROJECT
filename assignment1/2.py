import random as r
i = 1;
while(1):
	print("enter 1 to play\nenter 0 to quit")
	i = int(input())
	if(i == 0):
		break
	elif(i == 1):
		print(r.randint(1,6))


