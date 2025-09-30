"""Regex helpers to parse common log-like lines.
This parser is intentionally simple and works with the sample.log format included.
Expected format (example):
2025-09-30 12:34:56,789 - ERROR - 192.168.1.10 - Failed login for user 'admin'
"""
import re

LOG_RE = re.compile(r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}(?:,\d+)?)\s*-\s*(?P<level>[A-Z]+)\s*-\s*(?P<ip>\d{1,3}(?:\.\d{1,3}){3})\s*-\s*(?P<message>.*)')

def parse_common_log_line(line: str) -> dict:
    m = LOG_RE.search(line)
    if not m:
        return {"raw": line}
    return m.groupdict()
