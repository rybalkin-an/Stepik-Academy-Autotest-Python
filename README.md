:mortar_board: Stepik Academy. Автоматизация тестирования на Python.

Запуск тестов выполняется через командную строку командами:
pytest -v --tb=line --language=en --alluredir=allure_report -m need_review
pytest -v --tb=line --language=en --alluredir=allure_report -m need_review_custom_scenarios

Для отчета Allure выполнить команду:
allure serve allure_report
