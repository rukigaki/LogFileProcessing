import argparse
from pathlib import Path



class EngineParse:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("--file", help="Путь к CSV-файлу для обработки.")
        self.parser.add_argument("--report", help="Фильтрация строк по условию.")
        self.args = self.parser.parse_args()

    @property
    def get_file_path(self) -> Path:
        return Path(self.args.file)

    @property
    def get_report_value(self) -> str:
        return self.args.report