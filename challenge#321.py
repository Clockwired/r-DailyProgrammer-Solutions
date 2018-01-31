# https://www.reddit.com/r/dailyprogrammer/comments/6jr76h/20170627_challenge_321_easy_talking_clock/
# This is the challenge if ever to refer back to it.

#Check
p = 12
l = 0

'''Checks and outputs 24 hour time'''
def twelve_hour_time_fix(x, n):
	if type(x) == int and type(n) == int:
		if x == 0:
			return("BAWK BAWK STOP IT")
		elif n == 0 and x <= 12:
			return ("it's " + x + " oh clock")
		elif n > 0 and n < 10 and x <= 12:
			return("it's " + str(x) + " oh " + "0" + str(n) )
		elif n > 0 and n >= 10 and n < 60 and x <= 12:
			return(x + " oh" + n)
		elif x > 12:
			return("error, please use 12 hour time")
	else: 
		return("oh noes, there's an error, actually use non float and non string inputs!")

#The above function is to show the evolution of my thinking process

''' This is the better version of my above function '''
def twenty_four_hour_time_fix(x, n):
	meridian = 'a.m'
	if type(x) == int and type(n) == int:
		if x == 0:
			return("Error")
		elif x > 12:
			x = x - 12
			meridian = 'p.m'
			if x > 12:
				return("Error")
			elif x == 12 and n < 10 and n > 0:
				return("It's " + str(x) + " oh 0" + str(n) + " " + "p.m")
			elif x == 12 and n < 60 and n >= 10:
				return("It's " + str(x) + " oh " + str(n) + " " + "p.m")
			elif x <= 12 and n < 10 and n > 0:
				return("It's " + str(x) + " oh 0" + str(n) + " " + str(meridian))
			elif x <= 12 and n >= 10 and n < 60:
				return("It's " + str(x) + " oh " + str(n) + " " + str(meridian))
			elif x <= 12 and n == 0:
				return("It's " + str(x) + " " + str(meridian))
			elif x <= 12 and n == 0:
				return("error")
		else:
			if x <= 12 and n == 0:
				return("It's " + str(x) + " " + str(meridian))
			elif x <= 12 and n < 10:
				return("It's " + str(x) + " oh 0" + str(n) + " " + str(meridian))
			elif x <= 12 and n >= 10 and n < 60:
				return("It's " + str(x) + " oh " + str(n) + " " + str(meridian))
			elif n > 60:
				return("Error")
			else:
				return("Oh Noes")

print(twenty_four_hour_time_fix(p, l))

