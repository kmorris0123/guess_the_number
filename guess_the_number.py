import random


print("----------------Guess The Number----------------")
if input('To start the game please type "Yes" or "No": ') == "yes":

	run_game = True
	checker = True
else:
	print("Thanks for playing!")
	run_game = False


def number_generator():
# this is where the number is generated 
	gen_num = random.randint(0,100)
	
	return gen_num


def user_guess():
	usr_num = int(input("Guess a number between 1 and 100: "))

	
	return usr_num


def count():
	guess_count = 0
	guess_count += 1
	
	return guess_count

gen_num = number_generator()

while run_game == True:


	usr_num = user_guess()
	guess_count = count()
	
		
		

	if  int(gen_num) == int(usr_num) :

		print("You guessed correctly!")

		play_again = input('Do You want to play again? - "Yes" or "No" ')

		if play_again == "yes":
			gen_num = number_generator()
			usr_num = user_guess()
			guess_count = count()
		else: 
			print("Thank you for playing")
			run_game = False

	elif gen_num > usr_num:
		print("You guessed too low!")

	elif gen_num < usr_num:
		print("You guessed too high!")

	elif guess_count % 5 == 0:

		print("You have guessed " + guess_count + " times!")

	else:

		print('This input did not work, try again')
		usr_num = user_guess()




























