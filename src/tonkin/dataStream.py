import data
import arrays

def calculatePacketLength(variables):
	# Starts at 4 because time is stored in a single
	packetLength = 4
	for variable in variables:
		length = data.typeLengths[variable["Type"]]
		packetLength += length
	return packetLength

# Given a data stream and the list of variable types,
# get a list of packets from the data stream
def splitStreamToPackets(stream, variables):
	packetLength = calculatePacketLength(variables)
	return arrays.splitArrayIntoLengths(stream, packetLength)
