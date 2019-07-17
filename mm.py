import win32com.client as wincl
import random
import numpy as np
speak = wincl.Dispatch("SAPI.SpVoice")

def multiplication(lower = 1, upper = 99):
	T = True
	count = 0
	while T:
		
		a = np.random.randint(lower,upper)
		b = np.random.randint(lower,upper)
		answer = int(a*b)
		speak.Speak(str(a) + "times" + str(b))
		x = input("Answer? : ")
		if int(x) == answer:
			print("Correct! ")
			speak.Speak("Correct!\n")
			count+= 1
			print('Number Correct :',count)
		else:
			print("Wrong Dumbass ", answer)


		z = input("Again (Enter for Yes, type anything to Quit! ")
		if z == "":
			T == True
		else:
			T == False
			return 0


def addition(lower = 1, upper = 999):
	T = True
	while T:
		a = np.random.randint(lower,upper)
		b = np.random.randint(lower,upper)
		answer = int(a+b)
		speak.Speak(str(a) + "plus" + str(b))
		x = input("Answer? : ")
		if int(x) == answer:
			print("Correct! ")
			speak.Speak("Correct!")
		else:
			print("Wrong Dumbass ", answer)


		z = input("Again (Enter for Yes, type anything to Quit! ")
		if z == "":
			T == True
		else:
			T == False
			return 0

def subtraction(lower = 1, upper = 999):
	T = True
	while T:
		a = np.random.randint(lower,upper)
		b = np.random.randint(lower,upper)
		answer = int(a-b)
		speak.Speak(str(a) + "minus" + str(b))
		x = input("Answer? : ")
		if int(x) == answer:
			print("Correct! ")
			speak.Speak("Correct!")
		else:
			print("Wrong Dumbass ", answer)


		z = input("Again (Enter for Yes, type anything to Quit! ")
		if z == "":
			T == True
		else:
			T == False
			return 0

def division(lower = 1, upper = 999):
	T = True
	while T:
		a = np.random.randint(lower,upper)
		b = np.random.randint(lower,upper)
		question = int(a*b)
		speak.Speak(str(question) + "over " + str(a))
		x = input("Answer? : ")
		if int(x) == b:
			print("Correct! ")
			speak.Speak("Correct!")
		else:
			print("Wrong Dumbass ", b)


		z = input("Again (Enter for Yes, type anything to Quit! ")
		if z == "":
			T == True
		else:
			T == False
			return 0


def main_loop():
	T = True
	while T:

		user_inp = input("Select your Operation, + (1), - (2), * (3), / (4): ")
		u = input("Choose upper bound ")
		l = input("Choose lower bound ")
		if user_inp == str(1):
			addition(lower = l, upper = u )
		if user_inp	== str(2):
			subtraction(lower = l, upper = u)
		if user_inp == str(3):
			multiplication(lower = l, upper = u)
		if user_inp == str(4):
			division(lower = l, upper = u)
		new = input("Would you like to continue (y/n)? ")
		if new == 'y':
			T = True
		else:
			T = False
			break 


if __name__ == '__main__':

	main_loop()