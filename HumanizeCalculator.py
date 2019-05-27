first_ten = ["", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen"]
other_tens = ["", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def convert(number, x, Flag):
    """ Функция для перевода с числа в слово"""
    n = number // x
    t = [first_ten[n], "hundred"] if n > 0 else []

    n = (number % x) // (int(x / 10))
    t += [other_tens[n - 1]] if n > 1 else []

    n = number // int(x / 100) % (10 if n > 1 else 20)
    t += [first_ten[n], Flag] if n > 0 else [Flag]

    return ' '.join(t)

def converter_(number):
    """"
    Основная рекурсивная функция,которая вызывается в том случае,если число не равно нулю
    Работает для чисел меньше 10**12 (trillion)
    Flag - это разряд числа: миллион,миллиард,тысяча.
    x - значение равное верхнему ограничению, деленное на 10
    """
    if 10**9 <= number < 10**12:
        x = 10**11
        Flag = "billion"
        return convert(number, x , Flag) + ", " + converter_(number % 10**9)

    elif 10**6 <= number < 10**9:
        x = 10**8
        Flag = "million"
        return convert(number, x , Flag) + ", " + converter_(number % 10**6)

    elif 10**3 <= number < 10**6:
        x = 10**5
        Flag = "thousand"
        return convert(number, x , Flag) + ", " + converter_(number % 10**3)

    else:
        x = 10**2
        Flag = ""
        return convert(number, x, Flag)

def converter(number):
    """
    Если число не равно нулю,вызываем функцию converter_(),которая работает с числом
    Если число больше 10**12,то поднимаем исключение (можно конечно сделать и для чисел больше,но есть ли смысл в этом )
    """
    if number >= 10**12:
        raise ValueError("Valid input.Integer number is too large")
    elif number == 0:
        return "zero"

    converted_number = converter_(number)

    if converted_number[-2:] == ", ":               # удаляем лишние запятые и пробелы,если они присутствуют
        converted_number = converted_number[:-2]
    elif converted_number[-1] == " ":
        converted_number = converted_number[:-1]    # удаляем лишние запятые и пробелы,если они присутствуют

    return converted_number

def hum_calc(string):
    """
    Функция,которая проходится по строке и переводит данную строку в слова
    Проверяет на наличие лишних символов,по типу букв,скобок (в данном коде скобки не обрабатываются), символов
    """
    result = ""
    previous = ""
    operations = {"+":"plus ", "-":"minus ", "/":"divide by ", "=":"equals ", "*":"multiply "}
    for i in string:
        if i.isdigit():
            previous += i
        elif i in "+-/*=":
            result += converter(int(previous))
            previous = ""
            result += " " + operations[i]
        elif i != " ":                                  # все остальные случаи,т.к числа и знаки уже проверили. Пробел пропускаем
            raise ValueError("Invalid input.")

    result += converter(int(previous))
    return result

#print(hum_calc("1 + 2 = 3"))

