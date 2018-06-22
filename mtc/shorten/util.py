import base64
import functools
import inspect
import os
import struct

from django.utils import encoding
from django.conf import settings


def decode(identifier: str) -> int:
    pad_size = len(raw_identifier) % 3
    return base64.b64decode(identifier + '=' * pad_size)


def encode(identifier: int) -> str:
    return base64.b64encode(identifier).rstrip('=')