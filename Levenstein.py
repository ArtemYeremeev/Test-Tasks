"""MIPT Python Course Lections 11-12"""


def levenstein(a, b):
    """"Функция, определяющая кратчайшее
    редакционное растояние между 2 строками"""
    f = [[(i + j) if i * j == 0 else 0 for j in range(len(b) + 1)]for i in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b [j - 1]:
                f[i][j] = f[i - 1][j - 1]
            else:
                f[i][j] = 1 + min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1])
    return f[len(a)][len(b)]


print('Расстояние Левенштейна -', levenstein('Кризис', 'Круиз'))
