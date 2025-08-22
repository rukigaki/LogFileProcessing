from enum import Enum


class AverageReport(Enum):
    HANDLER = "handler"
    TOTAL = "total"
    AVG_RESPONSE_TIME = "avg_response_time"

class ReportParam(Enum):
    AVERAGE = "average"
    ...

class JSON(Enum):
    URL = "url"
    RESPONSE_TIME = "response_time"
    ...