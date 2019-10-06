# Humanize Calculator
Converting math expressions with integer numbers to words.

## ABOUT

Конвертация математических выражений,которые могут включать в себе цифры, математические операции +,-,*,/,=, в слова.
В строке могут быть пробелы (не обязательно).Все числа типа integer (not float).
Если строка не валидна,возвращаем ValueError(Invalid input).

## ОГРАНИЧЕНИЯ
допустимые символы - '0...9', '+', '-', '*', '/', '=', ' ';
Числа принимаются до триллиона 10**12

## RUNNING

To run function use hum_calc(string)
Examples: print(hum_calc("1 + 2 = 3"))
Result: "one plus two equals three"

To run pytest file:
cd ~\Humanize_Calculator
pytest test_testpy.py -v   
