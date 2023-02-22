from enum import Enum


class FileSize(str, Enum):
    """Constants for file sizes"""

    GB = "gb"
    MB = "mb"
    KB = "kb"


def convert_file_size(
    value: int, file_type_one: FileSize, file_type_two: FileSize
) -> int:
    """Converts either file sizes of mb, kb, and gb"""

    # Map of file sizes and the amount of bytes each is

    file_type_bytes = {
        FileSize.KB: 1000,
        FileSize.MB: 1000**2,
        FileSize.GB: 1000**3,
    }

    # Getting the amount of bytes the given value is with its file size
    # Dividing the amount with the size of the conversion metric
    amount_of_bytes = value * file_type_bytes[file_type_one]
    converted_metric = amount_of_bytes // file_type_bytes[file_type_two]

    return converted_metric
