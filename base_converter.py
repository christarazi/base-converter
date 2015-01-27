import sys

def convertStrToInt(numString):

	"""
	Parses the string and converts the characters into individual base 10 values.
	Values are placed in a list in the same order as numString and returned.
	Algorithm is based off strtol.c.
	"""

	l = []

	# If numString is prefixed with '-', remove it first then parse out '0x'.
	if numString[0] == '-':
		if numString[1] == '0' and (numString[2] == 'x' or numString[2] == 'X'):
			numString = numString[3:]
			numString = '-' + numString
	if numString[0] == '0' and (numString[1] == 'x' or numString[1] == 'X'):
		numString = numString[2:]

	for i in numString:
		if i == '-':
			l.append('-')
		elif i.isdigit():
			l.append(ord(i) - ord('0'))
		elif i.isalpha() and i.isupper():
			l.append(ord(i) - ord('A') + 10)
		elif i.isalpha() and i.islower():
			l.append((ord(i) - ord('a') + 10))
		else:
			break

	return l

def convertToBase10(numList, base):

	"""
	Parses numList and returns the total base 10 value in the list.
	"""

	negative = False

	# If numList contains a negative, then remove it...
	# and indicate it is negative so the algorithm can continue.
	if numList[0] == '-':
		numList.remove('-')
		negative = True

	numList = numList[::-1]
	if negative:
		for i in range(len(numList)):
			numList[i] *= -1
			numList[i] *= (base ** i)
	else:
		for i in range(len(numList)):
			numList[i] *= base ** i

	return sum(numList)

def convertToAnyBase(n, base):

	"""
	Converts n to whichever base is indicated. Algorithm can be found here:
	https://en.wikipedia.org/wiki/Negative_base#Calculation
	"""

	characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	i = 0
	s = ''

	if n > 0:
		while n != 0:
			remainder = n % base
			n //= base
				
			if remainder < 0:
				remainder += abs(base)
				n += 1

			s += characters[remainder]
			i += 1

		return s[::-1]				# return reversed string

	elif n < 0 and base > 0:
		while n != 0:
			remainder = n % base
			n = (abs(n) // base) * -1 		# e.g. -5 // 2 = -3, we want -2 instead; must use absolute value

			if remainder < 0:
				remainder += abs(base)
				n += 1

			s += characters[remainder]
			i += 1

		return '-' + s[::-1]		# return reversed string prefixed with minus sign

	elif n < 0 and base < 0:
		while n != 0:
			remainder = n % base
			n //= base

			if remainder < 0:
				remainder += abs(base)
				n += 1

			s += characters[remainder]
			i += 1

		return s[::-1]				# return reversed string


def main():
	numString = sys.argv[1]
	baseIn = int(sys.argv[2])
	baseOut = int(sys.argv[3])

	if (baseIn > 36 or baseOut > 36) or (baseIn == 0 or baseOut == 0) or (baseIn == baseOut):
		print("Program doesn't support the bases you inputted. Exiting...")
		raise SystemExit    

	print("Input: " + numString + " base " + str(baseIn) + ".")

	n = convertToBase10(convertStrToInt(numString), baseIn)

	if baseOut == 1:
		ones = str(1) * n
		print("Output: " + str(ones) + " base " + str(baseOut) + ".")
	elif baseOut == -1:
		ones = str(1) * n
		print("Output: -" + str(ones) + " base " + str(baseOut) + ".")
	else:
		# If both bases are ten then we have already calculated its value.
		if abs(baseIn) == 10 and abs(baseOut) == 10:
			print("Output: " + str(n) + " base " + str(baseOut) + ".")
		elif abs(baseOut) == 10:
			print("Output: " + str(n) + " base " + str(baseOut) + ".")
		else:
			print("Output: " + str(convertToAnyBase(n, baseOut)) + " base " + str(baseOut) + ".")

if __name__ == "__main__":
	main()
