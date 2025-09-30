"""Iterator and generator utilities for log files"""
import os

class LogFileIterator:
    """Iterator that reads a file line-by-line (memory efficient)."""
    def __init__(self, path, encoding="utf-8"):
        if not os.path.exists(path):
            raise FileNotFoundError(path)
        self.path = path
        self.encoding = encoding
        self._file = None

    def __iter__(self):
        self._file = open(self.path, "r", encoding=self.encoding)
        return self

    def __next__(self):
        if self._file is None:
            self._file = open(self.path, "r", encoding=self.encoding)
        line = self._file.readline()
        if line == "":
            self._file.close()
            raise StopIteration
        return line.rstrip("\n")

def error_lines_generator(iterator):
    """Generator that yields lines which look like errors or warnings.
    A simple heuristic: lines containing 'ERROR' or 'WARN' (case-insensitive).
    """
    for line in iterator:
        if "error" in line.lower() or "warn" in line.lower():
            yield line
