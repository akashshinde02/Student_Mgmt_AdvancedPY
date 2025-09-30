"""AccessLogProcessor - example of another processor (not used by main by default)"""
from processors.base import LogProcessor
from utils.regex_utils import parse_common_log_line
from collections import Counter

class AccessLogProcessor(LogProcessor):
    def __init__(self):
        self.counter = Counter()

    def process_line(self, line: str):
        data = parse_common_log_line(line)
        ip = data.get("ip","UNKNOWN")
        self.counter[ip] += 1

    def summary(self) -> dict:
        return {"top_ips": dict(self.counter.most_common(10))}
