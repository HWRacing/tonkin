import struct

def convertint8(int8B: bytearray) -> int:
	return int.from_bytes(int8B, "little", signed=True)

def convertint16(int16B: bytearray) -> int:
	return int.from_bytes(int16B, "little", signed=True)

def convertint32(int32B: bytearray) -> int:
	return int.from_bytes(int32B, "little", signed=True)

def convertuint8(uint8B: bytearray) -> int:
	return int.from_bytes(uint8B, "little", signed=False)

def convertuint16(uint16B: bytearray) -> int:
	return int.from_bytes(uint16B, "little", signed=False)

def convertSingle(singleB: bytearray) -> float:
	return struct.unpack("f", singleB)[0]

def convertBoolean(boolB: bytearray) -> bool:
	if boolB == b'\x01':
		return True
	else:
		return False
