from sendSignal import makeSignal
from decode import decode

def sendAck(b):
	if b:
		makeSignal("1")
	else:
		makeSignal("0")

def decodeAtReceiver(s):
	if (len(s)<16):
		print("Incorrect input sequence")
		return
	decoded = decode(s)
	if decoded != False:
		print ("Message has been receieved correctly!")
		print 
		print ("Message is " + decoded)
		print
		sendAck(True)
		return True
	else:
		print("Error detected in message")
		print
		sendAck(False)
		return False


if __name__=="__main__":
	while True:
		st = raw_input("Please input the receieved data: ")
		if decodeAtReceiver(st):
			break
		