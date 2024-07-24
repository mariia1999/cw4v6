from src.hh_api import HeadHunter
from src.vacancy import Vacancy
from src.json_classes import JSONSaver


def get_salary():

    while True:
        salary = input('Введите диапозон зарплат в формате "минимальная зарплата - максимальная зарплата": ')
        try:
            min_salary_str, max_salary_str = salary.split(' - ')
            min_salary = int(min_salary_str)
            max_salary = int(max_salary_str)
            if min_salary > max_salary:
                raise ValueError
            return min_salary, max_salary
        except ValueError:
            print('Неправильно введен диапозон. Пожалуйста, введите зарплаты в формате "минимальная зарплата - максимальная зарплата"')


def get_vacancies_by_salary(min_salary, max_salary):
    result = []
    saver = JSONSaver()
    all_vacancies = saver.get_vacancies()

    for vac in all_vacancies:
        salary_from = vac.salary_from
        salary_to = vac.salary_to

        if salary_from >= min_salary and salary_to <= max_salary:
            result.append(vac)
    return result


def filter_keywords():
    result = []
    saver = JSONSaver()
    all_vacancies = saver.get_vacancies()

    for vacancy in all_vacancies:
        if vacancy in Vacancy.name:
            result.append(vacancy)
    return result


def get_top(result, top_n):
    try:
        if top_n:
            if int(top_n) == 0:
                raise IndexError(f"\n\nВы передали некорректное значение - {top_n}\n"
                                 f"Ошибка: невозможно вернуть {top_n} вакансий")
            else:
                raise IndexError(f"\n\nПо указанным параметрам мы нашли только {len(result)}")
    finally:
        return result[:int(top_n)]


def print_vacancies(result):
    for el in result:
        print(el)


if __name__ == "__main__":
    main()
