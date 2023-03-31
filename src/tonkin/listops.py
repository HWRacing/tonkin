from typing import List, Any

def shiftListLeft(input: List[Any], shift: int) -> List[Any]:
	# Bring large numbers down to smaller equivalents
	# and handle negatives for shifts right
	shift = shift % len(input)

	for i in range(0, shift):
		input.append(input.pop(0))
	return input