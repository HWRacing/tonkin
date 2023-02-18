from .arrays import splitArrayBySub

def splitVariables(variableSection):
	return splitArrayBySub(variableSection, [0x43, 0x43, 0x3E])

def extractVariableName(variableDefinition):
	outputBytes = []
	# Remove data before variable name
	variableDefinition = variableDefinition[66:]

	# Extract name
	for i in variableDefinition:
		if i == 0x00:
			break
		outputBytes.append(chr(i))

	return "".join(outputBytes)
