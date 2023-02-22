def _checkIfFixedIsSigned(typeString):
	if typeString[0] == "u":
		signed = 0
	elif typeString[0] == "s":
		signed = 1
	else:
		raise ValueError("Sign indication not found in type string")
	return signed

def _getWordLength(typeString):
	# Remove unneccessary data
	typeString = typeString[4:]
	typeString = typeString.split("_")
	return int(typeString[0])

# TODO: Check if negative total slopes possible?
def _getTotalSlope(typeString):
	totalSlope = 1
	if "S" in typeString:
		totalSlopeIndex = typeString.index("S") + 1
		totalSlope = int(typeString[totalSlopeIndex])
	elif "E" in typeString:
		totalSlopeIndex = typeString.index("E") + 1
		totalSlope = 2 ** int(typeString[totalSlopeIndex])
	return totalSlope

# TODO: Check if negative biases possible?
def _getBias(typeString):
	bias = 0
	if "B" in typeString:
		biasIndex = typeString.index("B") + 1
		bias = int(typeString[biasIndex])
	return bias

def getFixedType(typeString):
	signed = _checkIfFixedIsSigned(typeString)
	wordLength = _getWordLength(typeString)
	totalSlope = _getTotalSlope(typeString)
	bias = _getBias(typeString)
	return signed, wordLength, totalSlope, bias
	
