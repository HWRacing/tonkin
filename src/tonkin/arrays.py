def shiftArrayLeft(array, shift):
	# Bring large numbers down to smaller equivalents
	# and handle negatives for shifts right
	shift = shift % len(array)

	for i in range(0, shift):
		array.append(array.pop(0))
	return array
