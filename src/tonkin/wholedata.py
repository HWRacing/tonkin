import arrays

# Returns the header section of a file
def extractHeaderSec(fileBytes):
	return fileBytes[0:228]

def extractVariablesSec(fileBytes):
	output = fileBytes[228:]
	end = arrays.getSubArrayIndex(output, [0x43, 0x47, 0x1A])
	return output[:end]
