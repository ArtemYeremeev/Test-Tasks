from openpyxl import load_workbook
import random
"""
Программа, отбирающая 100 случайных значений из 
предложенного списка и формирует новый список 
"""
# Используя openpyxl из исходного файла формата .xlsx извлекается необходимый столбец
source_data = load_workbook('test_task.xlsx')
data = source_data['test_task']
column_b = data['A']
# Создается пустой список для размещения данных
sample = []
# Используя цикл for и операцию append значения столбца переносятся в созданный список
for i in range(len(column_b)):
    cell = column_b[i].value
    sample.append(cell)
# При необходимости значения могут быть проверены
check = input('Значения получены. Хотите посмотреть? (да/нет)')
if check == 'да':
    print(sample)
else:
    pass
# Функция ввода запрашивает требуемое число значений
n = int(input('Сколько значений вам требуется?'))
# Создается новый пустой список для размещения данных
numbers = []
# С помощью random в цикле for заполняется новый список
for x in range(n):
    a = random.choice(sample)
    numbers.append(a)
# Выводится конечный результат
print(numbers)
