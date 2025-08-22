from abc import ABC, abstractmethod


class Aggregate(ABC):


    @abstractmethod
    def report(self, data) -> dict[str, list]:
        """
        Абстрактный метод для создания Операций, которые будут применены для манипуляции с таблицей
        Example: aggregate, order_by, sorting и т.д.

        :param data: Это распарсенный csv-файл, который является списком словарей
        Example: [{"brand": "apple", "price": "100", "rating": "4.5"},
                {"brand": "samsung", "price": "200", "rating": "3.5"}]


        :return: Возвращает уже готовый объект в orchestrator.py, который вызывается в main.py(точка входа)
        """
        pass