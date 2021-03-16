import typing
import zipfile
import struct
from zlib import crc32

# pylint:disable=protected-access

u4 = struct.Struct("<L")

CRC_OFFSET = 14


def updateCRC(archive: zipfile.ZipFile, fileInfo: zipfile.ZipInfo, crc: int) -> None:
	z.fp.seek(fi.header_offset + CRC_OFFSET)
	z.fp.write(u4.pack(crc))


def getCompressedFileContentsSlice(z: zipfile.ZipFile, fileName: str) -> slice:
	with z.open(fileName, "r") as r:
		pass

	s = r._orig_compress_start
	return slice(s, s + r._orig_file_size)


def replaceFile(archive: zipfile.ZipFile, fileInfo: zipfile.ZipInfo, newContent: typing.Union[bytes, bytearray, "mmap.mmap"]) -> None:
	if archive.mode != "a":
		raise ValueError("Archive must be in `a` mode")

	#if archive.compression != zipfile.ZIP_STORED or fileInfo.compress_type != zipfile.ZIP_STORED:
	if fileInfo.compress_type != zipfile.ZIP_STORED:
		raise Exception("Cannot replace: the file is compressed:", fileInfo.compress_type, archive.compression)

	bytesSlice = getCompressedFileContentsSlice(archive, fileInfo.filename)
	sz = bytesSlice.stop - bytesSlice.start

	sizeDelta = len(newContent) - sz
	if sizeDelta:
		raise ValueError("Size mismatch:", sz, sizeDelta)

	oldPos = archive.fp.tell()
	archive.fp.seek(bytesSlice.start)
	archive.fp.write(newContent)
	
	updateCRC(archive, fileInfo, crc32(newContent))
	archive.fp.seek(oldPos)
