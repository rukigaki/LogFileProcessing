import json

from parser.parser_engine import EngineParse
from aggregate_module import AverageHandler
from constants import JSON



class JSONAggregateInterface:
    def __init__(self) -> None:
        self.parsed_args = EngineParse()
        self.data = self.__prepare_data(
            file_path=self.parsed_args.get_file_path,
            date=self.parsed_args.get_date_value
        )

        self.average = AverageHandler()
        ...
        self.aggregate_functions = [self.average, ...]
        self.str_view_agg_func = [str(i) for i in self.aggregate_functions]


    def report(self, report_param) -> dict[str, list]:
        ind = self.str_view_agg_func.index(report_param)
        return self.aggregate_functions[ind].report(self.data)



    @staticmethod
    def __prepare_data(file_path, date) -> list[dict]:
        data = []

        with open(file_path) as file:
            str_jsons = file.readlines()
            for str_json in str_jsons:
                dict_obj = json.loads(str_json)
                data.append(dict_obj)
        try:
            data = [dict_obj for dict_obj in data if date in dict_obj[JSON.TIMESTAMP.value]]
        except TypeError:
            return data

        return data

