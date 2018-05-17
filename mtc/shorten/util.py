import base64
import struct

def decode(identifier: str) -> int:
    return base64.b64decode(identifier)


def encode(identifier: int) -> str:
    return base64.b64encode(identifier)