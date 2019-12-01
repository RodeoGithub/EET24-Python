"""This program simulate a log in with a constant user and password previously
declareted. Using while until a correct access or locked access. MAX ATTEMPTS: 3
"""
def a2():
	US="simon"
	PASS="programacion"
	UC=0
	PC=0
	c=0
	while(UC==0 or PC==0):
		user=input("Enter user: ")
		password=input("Enter password: ")
		if(user!=US):
			print("incorrect user")
			UC=0
		else:
			UC=1
		if(password!=PASS):
			print("incorrect password")
			PC=0
		else:
			PC=1
		c=c+1
		if(c>2):
			UC=-1
			PC=-1
		if(UC!=1 or PC!=1):
			print(c)
	if(UC==1 and PC==1):
		print("Correct access")
	else:
		print("Locked Access. Wait 30 minutes and try again")
