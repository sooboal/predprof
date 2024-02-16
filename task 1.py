with open('rocket.txt', 'r', encoding='utf8') as file:
    mas = list()
    ans = dict()
    for i in file:
        mas.append(i.strip().split('@'))
    for i in mas[1:]:
        if i[2] not in ans:
            ans[i[2]] = 1
        else:
            ans[i[2]] = ans[i[2]] + 1

with open('rocket_part.txt', 'w', newline='', encoding='utf8') as f:
    f.write('rocketPart@countCode')
    for i in ans:
        f.write(f"{i}@{ans[i]}")

a = input()
print(ans[a])
