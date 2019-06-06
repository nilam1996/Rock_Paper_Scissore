import random
my_list=["rock","paper","scissor"]
computer=random.choice(my_list)
print computer
while True:
	user_input=raw_input("Enter your n umber -")
	if user_input not in my_list:
		print "invalid"
	if user_input==computer:
		print "drow"
	elif user_input=="scissor" and computer=="rock":
		print "you are looser"
	elif user_input=="rock" and computer=="paper":
		print "you winner"
	elif user_input=="paper" and computer=="scissor":
		print "you are looser"
	elif user_input=="rock" and computer=="scissor":
		print "you are looser"
	elif user_input=="paper" and computer=="rock":
		print "you are winner"
	elif user_input=="scissor"and computer=="paper":
		print  "you winner "
	else:
		print "you are looser"
	raw_input1=raw_input("Enter y/n")
	if raw_input1=="y":
		continue
	elif raw_input1=="n":
		break


