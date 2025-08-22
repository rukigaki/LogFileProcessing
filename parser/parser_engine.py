import argparse
from pathlib import Path



class EngineParse:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("--file", help="Путь к .log-файлу, из которого будут распарсены JSON данные")
        self.parser.add_argument("--report", help="Тип агрегации и создание соответствущей таблицы")
        self.args = self.parser.parse_args()

    @property
    def get_file_path(self) -> Path:
        return Path(self.args.file)

    @property
    def get_report_value(self) -> str:
        return self.args.report