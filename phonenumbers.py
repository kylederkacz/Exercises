PHONE_NUMBER_LENGTH = 10

def phone(number):
	number = str(int(number))
	if len(number) < PHONE_NUMBER_LENGTH:
		raise Exception('Invalid phone number')
	def calcstrings(number, digit, string):
		if digit == PHONE_NUMBER_LENGTH:
			print string
		else:
			for i in 1,2,3:
				calcstrings(number, digit+1, string+get_char(int(number[digit]), i))
			
	calcstrings(number, 0, '')
	


# Get character method

chars = ( 
	('0', '0', '0'),
	('1', '1', '1'),
	('A', 'B', 'C'),
	('D', 'E', 'F'),
	('G', 'H', 'I'),
	('J', 'K', 'L'),
	('M', 'N', 'O'),
	('P', 'R', 'S'),
	('T', 'U', 'V'),
	('W', 'X', 'Y'),
)

def get_char(digit, place):
	if digit >= len(chars):
		raise Exception('Invalid digit')
	if place > 3 or place < 1:
		raise Exception('Invalid character location.')
	return chars[digit][place-1]


phone(5126187802)
