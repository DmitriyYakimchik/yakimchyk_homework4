# Dzmitry Yakimchyk
# Homework-4
# 16.06.2023
# Grodno-IT-Academy-Python 3.11

# теперь тесты написаны с использованием библиотеки pytest
# нам нужно ее установить: pip install pytest
# и запустить как обычный файл: pytest test_Homework4.py


def fibonacci(n: int) -> int:
    # Выведите n-ое число Фибоначчи, используя только временные переменные, циклические операторы и условные операторы. n - вводится.
    fib, fir_sup = 1, 1

    for i in range(0, n):
        if i != 0:
            # текущий равен сумме 2-х предыдущих
            sum_fib = fir_sup + fib
            # предпоследний найденный
            fir_sup = fib
            # последний найденный
            fib = sum_fib
        else:
            fib = 0
    return fib


def palindrome(n: int) -> bool:
    # Определите, является ли число палиндромом (читается слева направо и справа налево одинаково). Число положительное целое, произвольной длины. Задача требует работать только с числами (без конвертации числа в строку или что-нибудь еще).
    """Берем последнее число делением с остатком на 10 и так пока он есть"""
    new_n = n % 10
    compare_n = n
    n //= 10
    while n != 0:
        new_n = new_n * 10 + n % 10
        n //= 10
    if compare_n == new_n:
        print(f'{compare_n}-{new_n}')
        return True
    else:
        print(f'{compare_n}-{new_n}')
        return False
# palindrome(11)


def fizz_buzz(S: int, N: int):
    # Напишите генератор, который возвращает цифры от S до N, но вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz.
    if S <= N:
        step = 1
        N += 1
    else:
        step = -1
        N -= 1
    for i in range(S, N, step):
        if i % 3 == 0 and i % 5 == 0:
            phrase = 'FizzBuzz'
        elif i % 3 == 0:
            phrase = 'Fizz'
        elif i % 5 == 0:
            phrase = 'Buzz'
        else:
            phrase = str(i)
        yield phrase

gen = fizz_buzz(100, 1)
for i in gen:
    print(i)
