# Отчет о выполнении задания промежуточной аттестации

## Код программы

Код программы размещен по ссылке: [Код программы](https://github.com/GeorgeKuzora/gb_home_work/blob/main/12_Testing/seminar6/src/average_utils.py)

## Код тестов

Код тестов размещен по ссылке: [Код тестов](https://github.com/GeorgeKuzora/gb_home_work/blob/main/12_Testing/seminar6/tests/test_average_utils.py)

## Отчет pylint

Отчет для файла `src/average_utils.py`

![average_utils pylint](pylint1.png)

Отчет для файла `tests/test_average_utils.py`

![test_average_utils pylint](pylint2.png)

## Отчет о покрытии тестами coverage

![coverage](coverage.png) 

## Объяснение принципа покрытия тестами

Программа состоит из двух статических методов. Метод compare_average вызывает метод find_average в ходе своей работы.

Я решил создать unit-тесты для метода find_average и для метода compare_average.

Для создания unit-тестов для метода compare_average, я использовал patch для статического метода find_average. Эта мера позволила устранить зависимость метода compare_average от статического метода find_average. Но в тоже время подобная мера сделала эти тесты хрупкими. Это произошло из-за того, что реализация возвращаемых значений при помощи side_effect сделала результат теста зависимым от того, в какой последовательности метод find_average вызывается внутри метода compare_average.

Также я создал интеграционные тесты для проверки совместной работы обоих методов.

Для проверки правильного вывода метода compare_average я использовал возможности библиотеки pytest. `capsys` перехватывает потоки стандартного вывода и ошибок. Он позволяет записать эти данные в объект и обращаться к ним в ходе теста.
