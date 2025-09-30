from log_iterator import LogFileIterator, error_lines_generator
import os

def write_temp_log(tmp_path):
    p = tmp_path / "temp.log"
    p.write_text("2025-09-30 12:00:00 - INFO - 127.0.0.1 - OK\\n2025-09-30 12:01:00 - ERROR - 127.0.0.1 - Fail\\n")
    return str(p)

def test_iterator_and_generator(tmp_path):
    path = write_temp_log(tmp_path)
    it = LogFileIterator(path)
    lines = list(it)
    assert len(lines) == 2
    gen = error_lines_generator(iter(lines))
    # generator expects an iterator that yields lines; using list iterator works
    gen_list = list(gen)
    assert any("ERROR" in l for l in gen_list)
