from abc import ABC, abstractmethod


class Aggregate(ABC):


    @abstractmethod
    def report(self, data) -> dict[str, list]:
        """
        Абстрактный метод для создания логики отображения по агрегирующей функции (реализован - average,
        но также есть возможность добавить что-то новое по типу (sum, max, min и т.д.))

        :param data: Это распарсенный log-файл, который содержит в себе json строки, они преобразованы в нативный для
        Python тип данных, список из словарей list[dict]

        Example: [
        {"@timestamp": "2025-06-22T13:57:32+00:00", "status": 200, "url": "/api/context/...", "request_method": "GET", "response_time": 0.024, "http_user_agent": "..."}
        {"@timestamp": "2025-06-22T13:57:32+00:00", "status": 200, "url": "/api/context/...", "request_method": "GET", "response_time": 0.02, "http_user_agent": "..."}
        ]


        :return: Возвращает tabular_data, это словарь такого типа

        Example: {
            "handler": list[str],
            "total": list[int],
            "avg_response_time": list[float]
            }
        """
        pass