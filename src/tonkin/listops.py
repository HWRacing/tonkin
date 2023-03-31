from typing import List, Any

def shiftListLeft(input: List[Any], shift: int) -> List[Any]:
	# Bring large numbers down to smaller equivalents
	# and handle negatives for shifts right
	shift = shift % len(input)

	for i in range(0, shift):
		input.append(input.pop(0))
	return input

# Given a source list and a target list, returns the index of where the target
# list appears within the source list (returns the index of the final value)
def getSubListIndex(source: List[Any], target: List[Any]) -> int:
	# TODO: Ensure that the buffer items don't appear in split
	buffer = [None] * len(target)
	
	for j, i in enumerate(source):
		buffer = shiftListLeft(buffer, 1)
		buffer[-1] = i

		if buffer == target:
			return j
	
	raise ValueError("Sub-list not found")

def getSubListIndices(source: List[Any], target: List[Any]) -> List[int]:
	output = []

	# TODO: Ensure that the buffer items don't appear in split
	buffer = [None] * len(target)
	
	for j, i in enumerate(source):
		buffer = shiftListLeft(buffer, 1)
		buffer[-1] = i

		if buffer == target:
			output.append(j)
	
	return output
