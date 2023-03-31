import tonkin.listops as lops
from typing import List, Union
from countach import measurement as mea
from countach import characteristic as cha

# Split the variables section into individual definitions
def splitVarSectionToDefs(varSection: bytearray) -> List[List[bytearray]]:
	return lops.splitListBySub(list(varSection), [0x43, 0x43, 0x3E])

# Extract a variable name from a definition
def extractVariableName(varDef: bytearray) -> str:
	outputBytes = []
	# Remove data before variable name
	varDef = varDef[66:]

	# Extract name
	for i in varDef:
		if i == 0x00:
			break
		outputBytes.append(chr(i))

	return "".join(outputBytes)

# Get a list of variable names from a list of definitions (ignores the last one)
def extractVariableNames(varDefs: List[bytearray]) -> List[str]:
	# Don't get the "time" variable
	varDefs.pop(-1)
	output = []
	for var in varDefs:
		output.append(extractVariableName(var))
	return output

def getTypeFromA2L(variableName: str, a2lData: List[Union[mea.Measurement, cha.Characteristic]]) -> str:
	for i in a2lData:
		rightCategory = type(i) == mea.Measurement
		rightName = i.name == variableName
		if rightCategory and rightName:
			return str(i.dataType)
	raise ValueError("Variable " + variableName + " not found in A2L data")
