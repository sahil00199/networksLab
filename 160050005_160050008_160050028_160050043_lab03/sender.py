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
		makeSignal(message)
	else:
		return 