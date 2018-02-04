crc = "111"

def calcCRC(arg1, arg2):
	if (len(arg1) < len(arg2)):
		return arg1
	if arg1[0] == '0':
		return calcCRC(arg1[1:], arg2)
	for i in range(len(arg2)):
		ll = list (arg1)
		# print(ord(arg1[i]))
		ll[i] = chr(((ord(arg1[i]) - 48) ^ (ord(arg2[i]) - 48))+48)
		arg1 = ''.join(ll)
	return calcCRC(arg1[1:], arg2)

def appendCRC(arg):
	return arg + calcCRC(arg+('0'*(len(crc) - 1)), crc)

