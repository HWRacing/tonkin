# Returns the header section of a file
def extractHeaderSec(fileBytes):
	return fileBytes[0:228]

# Get the index of the end of the variable definition section
# (as signalled by the bytes 43 47 1A)
def getEndOfVariableSec(bytesWithoutHeader):
	# Buffer of three bytes
	buffer = [0x00, 0x00, 0x00]
	
	for j, i in enumerate(bytesWithoutHeader):
		# Push bytes back one
		buffer[0] = buffer[1]
		buffer[1] = buffer[2]

		# Get new byte
		buffer[2] = i
		print(buffer)

		if buffer == [0x43, 0x47, 0x1A]:
			return j
	
	raise ValueError("Variable definition end bytes not found")

def extractVariablesSec(fileBytes):
	output = fileBytes[228:]
	end = getEndOfVariableSec(output)
	return output[:end]
