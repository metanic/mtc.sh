import base64
import functools
import inspect
import os
import struct

from django.utils import encoding
from django.conf import settings


def decode(identifier: str, password: str = None) -> int:
    pad_size = len(identifier) % 3
    b64_content = identifier + '=' * pad_size

    derived = base64.b64decode(b64_content)

    if password is None:
        return derived

    # TODO: Decrypt w/ password
    return derived


def encode(identifier: int, password: str = None) -> str:
    stored = base64.b64encode(identifier).rstrip('=')

    if password is None:
        return stored

    # TODO: Encrypt w/ password
    return stored