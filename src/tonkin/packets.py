import tonkin.datvar
import tonkin.values
from typing import List, Dict

def _splitPacket(rawPacket: bytearray, vars: List[tonkin.datvar.Datvar]) -> List[bytearray]:
	splitPacket = []
	for var in vars:
		splitPacket.append(rawPacket[:var.getLength()])
		rawPacket = rawPacket[var.getLength():]
	return splitPacket

def readRawPacket(rawPacket: bytearray, vars: List[tonkin.datvar.Datvar]) -> Dict:
	vals = _splitPacket(rawPacket, vars)
	packet = {}
	for index, var in enumerate(vars):
		varName = var.name
		value = tonkin.values.readRawValue(vals[index], var.dataType)
		packet[varName] = value
	return packet
