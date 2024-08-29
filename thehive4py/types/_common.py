from io import BytesIO
from os import PathLike

PathOrBuffer = str | PathLike | BytesIO
BufferOrNone = BytesIO | None
