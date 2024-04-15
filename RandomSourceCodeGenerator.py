import random
import re

def rearrange_code(source_code):
    # Находим все блоки кода, начинающиеся с def и заканчивающиеся :
    methods = re.findall(r'def.*?:', source_code, re.DOTALL)
    
    # Перемешиваем блоки методов случайным образом
    random.shuffle(methods)
    
    # Заменяем старые методы на перемешанные
    rearranged_code = re.sub(r'def.*?:', lambda _: methods.pop(0), source_code, count=len(methods))
    """
    # Находим все переменные результатов и их значения
    results = re.findall(r'(\bresult\d+\b)\s*=\s*.+', rearranged_code)
    
    # Перемешиваем переменные результатов и их порядок в вызове print
    random.shuffle(results)
    
    # Заменяем старые переменные результатов на перемешанные
    for i, result in enumerate(results):
        rearranged_code = re.sub(r'\bresult\d+\b\s*=\s*.+', result, rearranged_code, count=1)
    
          # Перемешиваем порядок переменных результатов в вызове print
    print_arguments = ', '.join(results)
    rearranged_code = re.sub(r'print\(.+\)', f'print({print_arguments})', rearranged_code)
    """
    return rearranged_code

source_code = """
class Number:
    def __init__(self, number):
        self.number = number
    
    def __add__(self, other):
        return self.number + other
    
    def __sub__(self, other):
        return self.number - other
    
    def __mul__(self, other):
        return self.number * other
    
    def __pow__(self, power, modulo=None):
        return self.number ** power
    
    def __truediv__(self, other):
        return self.number / other
    
    def __abs__(self):
        return abs(self.number)

num1 = Number(-10)
result1 = num1 + 90
result2 = num1 / 10
result3 = num1 * -1
result4 = num1 ** 2
result5 = num1 - 20
result6 = abs(num1)
print(result1, result2, result3, result4, result5, result6)
"""

# Перемешиваем исходный код
rearranged_code = rearrange_code(source_code)
print(rearranged_code)
