with open('rocket.txt', 'r', encoding='utf8') as file:
    mas = list()
    ans = dict()
    # Считываем файл
    for i in file:
        mas.append(i.strip().split('@'))
    for i in mas[1:]:
        # Если в словаре нет такого названия значит создаем новый
        if i[2] not in ans:
            ans[i[2]] = 1
        # Если есть то просто одбавляем единицу
        else:
            ans[i[2]] = ans[i[2]] + 1

with open('rocket_part.txt', 'w', newline='', encoding='utf8') as f:
    # Записываем ответ в файл
    f.write('rocketPart@countCode\n')
    for i in ans:
        f.write(f"{i}@{ans[i]}\n")

a = input()
print(ans[a])
