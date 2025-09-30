# Student_Mgmt_AdvancedPY
# LogAnalyzerSuite

Phase 3 - Advanced Python Engineering Studio
Real-time capstone: Log Analyzer & Utility Suite

## Features
- Memory-efficient iterator for log files
- Generator to filter error/warning lines
- Regex-based parsing for timestamp, level, ip, message
- Advanced OOP with abstract base class and processors
- Decorators for timing and simulated auth
- Uses os, sys, datetime, collections
- PyTest tests included in `tests/`

## Run
1. Ensure Python 3.8+ is installed.
2. From project root, run the sample:
```
python main.py logs/sample.log reports
```
3. Run tests:
```
pytest -q
```

## Extend ideas
- Add CSV/HTML report export
- Add more processors (AccessLogProcessor)
- Add CLI flags and logging
