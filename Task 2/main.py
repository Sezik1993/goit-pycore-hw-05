import re
from typing import Callable

def generator_numbers (text:str):
    # Пошук всих чисел з десятковою крапкою, які відокремлені пробілами
    pattern = r'\b\d+\.\d+\b'
    for match in re.findall(pattern, text):
        yield float(match)

def sum_profit(text: str, func:Callable):
    return sum(func(text))

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

# Виклик функцію
total_income = sum_profit(text, generator_numbers)

# Результат
print(f"Загальний дохід: {total_income}")

# запит /usr/local/bin/python3 "/Users/serhiikolomoiets/Desktop/neoversity /Home work/Python /goit-pycore-hw-05/goit-pycore-hw-05/Task 2/main.py"
# Відповідь: Загальний дохід: 1351.46
