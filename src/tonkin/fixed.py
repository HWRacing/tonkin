from typing import Tuple

def isSigned(typeStr: str) -> bool:
	if typeStr[0] == "u":
		signed = False
	elif typeStr[0] == "s":
		signed = True
	else:
		raise ValueError("Sign indication not found in type string")
	return signed

def getWordLength(typeStr: str) -> int:
	typeStr = typeStr[4:]
	splitTypeStr = typeStr.split("_")
	return int(splitTypeStr[0])

def getTotalSlope(typeStr: str) -> int:
	totalSlope = 1
	if "S" in typeStr:
		totalSlopeIndex = typeStr.index("S") + 1
		totalSlope = int(typeStr[totalSlopeIndex])
	elif "E" in typeStr:
		totalSlopeIndex = typeStr.index("E") + 1
		totalSlope = 2 ** int(typeStr[totalSlopeIndex])
	return totalSlope

def getBias(typeStr: str) -> int:
	bias = 0
	if "B" in typeStr:
		biasIndex = typeStr.index("B") + 1
		bias = int(typeStr[biasIndex])
	return bias

def getPropertiesFromFixedTypeStr(typeStr: str) -> Tuple[bool, int, int, int]:
	signed = isSigned(typeStr)
	wordLength = getWordLength(typeStr)
	totalSlope = getTotalSlope(typeStr)
	bias = getBias(typeStr)
	return signed, wordLength, totalSlope, bias

