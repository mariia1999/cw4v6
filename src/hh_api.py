from abc import ABC, abstractmethod
import requests
from requests import Response


class AbstractApi(ABC):
    @abstractmethod
    def get_response(self, text, per_page):
        pass

    @abstractmethod
    def get_vacancies(self, text, per_page):
        pass

    @abstractmethod
    def get_filter_vacancies(self, text, per_page):
        pass


class HeadHunter(AbstractApi):
    """Класс для работы с API hh.ru"""

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"

    def get_response(self, text: str, per_page: int) -> Response:
        """Запрос на API hh.ru"""
        params = {"text": f"NAME:{text}", "per_page": per_page, "page": 0}
        response = requests.get(self.__url, params=params)
        return response

    def get_vacancies(self, text: str, per_page: int) -> list:
        """Получение вакансий с hh.ru"""
        vacancies = self.get_response(text, per_page).json()["items"]
        return vacancies

    def get_filter_vacancies(self, text: str, per_page: int = 20) -> list:
        filtered_vacancies = []
        vacancies = self.get_vacancies(text, per_page)
        for vacancy in vacancies:
            filtered_vacancies.append({
                "name": vacancy["name"],
                "salary": vacancy["salary"],
                "url": vacancy["alternate_url"],
                "employer": vacancy["employer"]["name"]
            })
        return filtered_vacancies


