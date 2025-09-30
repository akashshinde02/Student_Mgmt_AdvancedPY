"""Helpers to write reports"""
import os, json, datetime

class ReportWriter:
    def __init__(self, out_dir="reports"):
        self.out_dir = out_dir

    def write_json(self, filename, data):
        path = os.path.join(self.out_dir, filename)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, default=str)
        return path

    def write_text(self, filename, text):
        path = os.path.join(self.out_dir, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        return path
