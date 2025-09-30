"""Process error log lines: regex parsing, counters, and summaries"""
import re
from collections import Counter, defaultdict
from processors.base import LogProcessor
from utils.regex_utils import parse_common_log_line

class ErrorLogProcessor(LogProcessor):
    def __init__(self):
        self.total = 0
        self.error_counter = Counter()
        self.ip_counter = Counter()
        self.by_date = defaultdict(int)

    def process_line(self, line: str):
        self.total += 1
        data = parse_common_log_line(line)
        # data may include 'level', 'ip', 'timestamp', 'message'
        level = data.get("level", "UNKNOWN")
        ip = data.get("ip", "UNKNOWN")
        ts = data.get("timestamp", None)
        self.error_counter[level] += 1
        self.ip_counter[ip] += 1
        if ts:
            self.by_date[ts.split(" ")[0]] += 1  # group by date

    def summary(self) -> dict:
        return {
            "total_error_lines": self.total,
            "errors_by_level": dict(self.error_counter.most_common()),
            "top_ips": dict(self.ip_counter.most_common(5)),
            "errors_by_date": dict(self.by_date)
        }
