import fileops
import countach
import wholedata
import variables
import dataStream
import packets

# Given a dat file and an a2l file, returns a list of dicts
# each representing a single packet
def readDatFileWithA2L(datFile, a2lFile):
	# Import the files
	a2lData = countach.extractData(a2lFile)
	fileBytes = fileops.importFile(datFile)
	# Split the dat file up into sections
	header, vars, stream = wholedata.splitFileData(fileBytes)
	# Extract the variables from the variable section
	variableList = variables.getVariableListFromA2L(vars, a2lData)
	rawPackets = dataStream.splitStreamToPackets(stream, variableList)
	output = []
	variableList.reverse()
	for packet in rawPackets:
		output.append(packets.readRawPacket(packet, variableList))
	return output
