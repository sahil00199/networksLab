from sendSignal import makeSignal
from appendCRC import appendCRC

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
		print ("Message is " + message)
		print
		sendAck(True)
		return
	else:
		print("Error detected in message")
		print
		sendAck(False)