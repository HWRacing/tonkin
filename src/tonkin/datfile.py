import tonkin.listops as lops

def extractHeaderSection(fileBytes: bytearray) -> bytearray:
	return fileBytes[0:228]

def extractVariablesSection(fileBytes: bytearray) -> bytearray:
	withoutHeader = fileBytes[228:]
	end = lops.getSubListIndex(list(withoutHeader), [0x43, 0x47, 0x1A])
	return withoutHeader[:end]

def extractDataSection(fileBytes: bytearray) -> bytearray:
	headerLength = len(extractHeaderSection(fileBytes))
	variableLength = len(extractVariablesSection(fileBytes))
	upperLength = headerLength + variableLength
	output = fileBytes[upperLength:]
	# The sequence of bytes that marks the start of the data stream
	startMarker = [0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
	# The index of the first byte of the data stream
	start = lops.getSubListIndex(list(output), list(startMarker)) + 1
	return output[start:]
