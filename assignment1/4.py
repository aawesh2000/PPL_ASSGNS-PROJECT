import random as r
while(1):
	print("Start game[1/0]")
	i = int(input())
	if(i == 0):
		break
	elif(i == 1):
		print("enter the range")
		x = int(input())
		num = r.randint(1,x)
		print("you have 5 chance to guess")
		for k in range(1, 6):
			j = int(input())
			if(j != num and k == 5):
				print('you lose... number was',num)
				break
			if(j < num and k != 5):
				print("HINT: number is greater")
			elif(j > num and k != 5):
				print("HINT: number is smaller")
			elif(j == num):
				print("yeah!!!! you got it right")
				break
			
			


