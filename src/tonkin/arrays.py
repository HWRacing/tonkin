def shiftArrayLeft(array, shift):
	# Bring large numbers down to smaller equivalents
	# and handle negatives for shifts right
	shift = shift % len(array)

	for i in range(0, shift):
		array.append(array.pop(0))
	return array

# Given a source array and a target array, returns the index of where the target
# array appears within the source array (returns the index of the final value)
def getSubArrayIndex(source, target):
	# TODO: Ensure that the buffer items don't appear in split
	buffer = [None] * len(target)
	
	for j, i in enumerate(source):
		buffer = shiftArrayLeft(buffer, 1)
		buffer[-1] = i

		if buffer == target:
			return j
	
	raise ValueError("Sub-array not found")
