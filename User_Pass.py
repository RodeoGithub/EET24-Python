"""This program simulate a log in with a constant user and password previously
declareted."""
def a1():
	US="simon"
	PASS="programacion"
	user=input("Enter user: ")
	password=input("Enter password: ")
	UC=0
	PC=0
	if(user!=US):
		print("Incorrect user")
	else:
		UC=1
	if(password!=PASS):
		print("Incorrect password")
	else:
		PC=1
	if(UC and PC):
		print("Correct access")
