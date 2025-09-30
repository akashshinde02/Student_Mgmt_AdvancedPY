"""LogAnalyzerSuite - CLI entry point"""
import sys, os, json
from log_iterator import LogFileIterator, error_lines_generator
from processors.error_processor import ErrorLogProcessor
from utils.report import ReportWriter
from utils.decorators import timeit

@timeit
def analyze_log(path, out_dir="reports"):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Log file not found: {path}")
    it = LogFileIterator(path)
    gen = error_lines_generator(it)
    proc = ErrorLogProcessor()
    for line in gen:
        proc.process_line(line)
    os.makedirs(out_dir, exist_ok=True)
    report = proc.summary()
    writer = ReportWriter(out_dir)
    report_path = writer.write_json("report.json", report)
    print(f"Report written to: {report_path}")
    return report_path

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <log_file_path> [report_dir]")
        sys.exit(1)
    path = sys.argv[1]
    out_dir = sys.argv[2] if len(sys.argv) > 2 else "reports"
    try:
        analyze_log(path, out_dir)
    except Exception as e:
        print("Error:", e)
        sys.exit(2)

if __name__ == "__main__":
    main()
