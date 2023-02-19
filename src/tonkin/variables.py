import arrays

def splitVariables(variableSection):
	return arrays.splitArrayBySub(variableSection, [0x43, 0x43, 0x3E])

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

# Temporary workaround because I haven't figured out
# how types are encoded in the EcoCAL data format
def getTypeFromA2LData(variableName, a2lData):
	for i in a2lData:
		rightCategory = i["Category"] == "Measurement"
		rightName = i["Name"] == variableName
		if rightCategory and rightName:
			return i["Type"]
	raise ValueError("Variable " + variableName + " not found in A2L data")

def matchWithA2LData(variableNames, a2lData):
	output = []
	for variable in variableNames:
		currentVar = {
			"Name": variable,
			"Type": getTypeFromA2LData(variable, a2lData)
		}
		output.append(currentVar)
	return output
