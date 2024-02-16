with open('rocket.txt', 'r', encoding='utf8') as file:
    mas = list()
    for i in file:
        mas.append(i.strip().split('@'))
    m = list()
    s = set()
    for i in mas:
        if i[2] not in s:
            x = [i[2], 0]
            h = 0
            for j in range(len(i[2])):
                h += ord(i[2][j]) * 67 ** j
            h %= 2 ** 16
            x[1] = h
            m.append(x)
            s.add(i[2])
    m = sorted(m, key=lambda x: x[1])
    print(m[:10])