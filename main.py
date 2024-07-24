from src.hh_api import HeadHunter
from src.vacancy import Vacancy
from src.utils import get_salary, get_vacancies_by_salary, filter_keywords, get_top
from src.json_classes import JSONSaver


def main():

    print('Добрый день! С помощью этого приложения поиск вакансий на hh.ru станет намного проще.')
    search = input("Введите ключевое слово для фильтрации вакансий: ").lower()
    min_salary, max_salary = get_salary()
    salary_range = get_vacancies_by_salary(min_salary, max_salary)
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))

    hh = HeadHunter()
    print('Получаем вакансии с сайта')
    vacancies = hh.get_vacancies(search, 30)
    vacancies_list = hh.get_filter_vacancies(vacancies, 30)
    print('Сохраняем вакансии в файл')
    saver = JSONSaver()
    saver.write_data(vacancies_list)

    filtered_vacancies = filter_keywords(vacancies_list, vacancies)
    range_vacancies = salary_range
    top_vacancies = get_top(range_vacancies, top_n)
    print(top_vacancies)


main()






