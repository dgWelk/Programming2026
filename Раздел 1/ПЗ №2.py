def start(item, name, target, statement):
    print(
        f'''
ПЗ №{item}, Винокуров А. В., ИБА-22
{name},
Цель: {target}
Постановка задачи: {statement}
''')

def price_for_1kg(kg, money):
    price_1kg = kg/money
    return price_1kg

def main():
    start(
        item=2,
        name='''Знакомство и работа с IDE PyCharm Community. Построение программ
линейной структуры в IDE PyCharm Community.''',
        target='''выработка первичных навыков работы с IDE PyCharm Community,
Git, GitGub, составление программ линейной структуры.''',
        statement='''Известно, что X кг шоколадных конфет стоит A рублей, 
а Y кг ирисок стоит B рублей. Определить, сколько стоит 1 кг шоколадных конфет,
1 кг ирисок, а также во сколько раз шоколадные конфеты дороже ирисок.''')

    x = float(input('Введите кол-во кг шоколадных конфет переменной >>> '))
    a = float(input('Введите цену за эти кг шкоколадных конфет >>> '))
    y = float(input(f'\nВведите кол-во кг ирисок переменной >>> '))
    b = float(input('Введите цену за эти кг шкоколадных конфет >>> '))

    print(f'''
Цена за 1 кг конфет: {price_for_1kg(x, a)} рублей,
Цена за 2 кг ирисок: {price_for_1kg(y, b)} рублей.
''')

main()