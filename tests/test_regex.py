from utils.regex_utils import parse_common_log_line

def test_parse_valid_line():
    line = "2025-09-30 12:34:56,789 - ERROR - 192.168.1.10 - Failed login for user 'admin'"
    data = parse_common_log_line(line)
    assert data["level"] == "ERROR"
    assert data["ip"] == "192.168.1.10"
    assert "Failed login" in data["message"]

def test_parse_invalid_line():
    line = "some random text not matching"
    data = parse_common_log_line(line)
    assert "raw" in data
