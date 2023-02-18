from .arrays import splitArrayBySub

def splitVariables(variableSection):
	return splitArrayBySub(variableSection, [0x43, 0x43, 0x3E])
