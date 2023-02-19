import data

def calculatePacketLength(variables):
	# Starts at 4 because time is stored in a single
	packetLength = 4
	for variable in variables:
		length = data.typeLengths[variable["Type"]]
		packetLength += length
	return packetLength
