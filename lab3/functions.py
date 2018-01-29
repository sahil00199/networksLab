from sendSignal import makeSignal
from appendCRC import appendCRC

def senderOriginal(s):
	s = appendCRC(s)
	sendSignal(s)

def sendAck(b):
	if b:
		makeSignal("1")
	else:
		makeSignal("0")

def decodeAtReceiver(s):
	if (len(s)<3):
		print("Incorrect input sequence")
		return
	crc = s[-2:]
	message = s[0:-2]
	if appendCRC(message)[-2:] == crc:
		print ("Message has been receieved correctly!")
		print 
		print ("Message is " + Message)
		print
		sendAck(True)
		return
	else:
		print("Error detected in message")
		print
		sendAck(False)

def senderResponse(m, s):
	if s == "0":
		makeSignal(m)
	else:
		return 