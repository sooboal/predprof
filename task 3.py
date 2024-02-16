with open('rocket.txt', 'r', encoding='utf8') as file:
    mas = list()
    for i in file:
        mas.append(i.strip().split('@'))
    a = input()
    while a != 'nlo':
        flag = True
        for i in mas:
            if a in i[2]:
                print(f"Шифр: {i[1]} от: {i[2]} был получен {i[0]}")
                flag = False
                a = input()
                break
        if flag:
            print('такой сигнал еще не был получен')
        a = input()
