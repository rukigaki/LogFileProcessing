from constants import AverageReport, JSON, ReportParam
from .abc_base import Aggregate



class AverageHandler(Aggregate):
    def __init__(self) -> None:
        self.tabular_data = {key.value: [] for key in AverageReport}

    def __str__(self) -> str:
        return ReportParam.AVERAGE.value


    @staticmethod
    def average(sum_, total) -> list[float]:
        average_value = [s / t for s, t in zip(sum_, total)]
        return average_value


    def report(self, data) -> dict[str, list]:
        for dict_obj in data:
            url = dict_obj[JSON.URL.value]
            response_time = dict_obj[JSON.RESPONSE_TIME.value]

            if url in self.tabular_data[AverageReport.HANDLER.value]:

                ind = self.tabular_data[AverageReport.HANDLER.value].index(url)

                self.tabular_data[AverageReport.TOTAL.value][ind] += 1
                self.tabular_data[AverageReport.AVG_RESPONSE_TIME.value][ind] += response_time

            else:
                self.tabular_data[AverageReport.HANDLER.value].append(url)
                self.tabular_data[AverageReport.TOTAL.value].append(1)
                self.tabular_data[AverageReport.AVG_RESPONSE_TIME.value].append(response_time)

        self.tabular_data[AverageReport.AVG_RESPONSE_TIME.value] = self.average(
            self.tabular_data[AverageReport.AVG_RESPONSE_TIME.value],
            self.tabular_data[AverageReport.TOTAL.value]
        )

        return self.tabular_data
