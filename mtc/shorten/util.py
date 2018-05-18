import base64
import struct

def decode(identifier: str) -> int:
    pad_size = len(identifier) % 3
    return base64.b64decode(identifier + '=' * pad_size)


def encode(identifier: int) -> str:
    return base64.b64encode(identifier.rstrip('='))
