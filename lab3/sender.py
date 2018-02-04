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


if __name__== "__main__":
	mes = raw_input("Please enter the message that you want to transmit: ")
	senderOriginal(mes)
	while True:
		response = raw_input("Please give us the message received from the receiver: ")
		if senderResponse(response):
			break