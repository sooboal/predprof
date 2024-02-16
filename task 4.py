def generate_number(number_by_date, code, name):
    """
    func name: generate_number
    :param number_by_date: Номер детали отсортированной по дате
    :param code: Код детали
    :param name: Название детали
    :return: Выводим полученный номер
    """

    ans = ''
    ans += str(number_by_date)
    ans += str(code)
    for _ in name.split(' '):
        ans += _[0]
    return ans


with open('rocket.txt', 'r', encoding='utf8') as file:
    mas = list()
    for i in file:
        mas.append(i.strip().split('@'))
    mas = sorted(mas, key=lambda x: x[0]) # сортируем по дате
    for i in range(len(mas)):
        mas[i].append(generate_number(i, mas[i][1], mas[i][2]))

with open('rocket_code.csv', 'w', newline='', encoding='utf8') as f:
    f.write('date@code@rocketparts@queue\n')
    for i in mas:
        f.write('@'.join(i) + '\n')
