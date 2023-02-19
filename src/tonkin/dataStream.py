import variables
import arrays

def _calculatePacketLength(vars):
	# Starts at 4 because time is stored in a single
	return 4 + variables.getVariableLengths(vars)

# Given a data stream and the list of variable types,
# get a list of packets from the data stream
def splitStreamToPackets(stream, vars):
	packetLength = _calculatePacketLength(vars)
	return arrays.splitArrayIntoLengths(stream, packetLength)
