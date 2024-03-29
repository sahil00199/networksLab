from sendSignal import makeSignal
from appendCRC import appendCRC

message=""

def senderOriginal(s):
	global message
	message = s
	s = appendCRC(s)
	makeSignal(s)

def sendIncorrect(correct, incorrect):
	crc = appendCRC(correct)[-2:]
	makeSignal(incorrect + crc)

def senderResponse(s):
	global message
	if s == "0":
		makeSignal(appendCRC(message))
		return False
	else:
		return True

def makeError(s, errors):
	s = list(s)
	for error in errors:
		if s[error] == '1':
			s[error] = '0'
		else:
			s[error] = '1'
	return ''.join(s)


if __name__== "__main__":
	message = raw_input("Please enter the message that you want to transmit: ")
	errors = raw_input("Please enter the indices of the errors: ").split()
	for i in range(len(errors)):
		errors[i] = int(errors[i])
	crc = appendCRC(message)[-2:]
	errorMes = makeError(message, errors)
	makeSignal(errorMes+crc)
	while True:
		response = raw_input("Please give us the message received from the receiver: ")
		if senderResponse(response):
			break