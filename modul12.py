per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Сумма вклада: "))

deposit = [round(float(money * i / 100), 2) for i in list(per_cent.values())]
print(deposit)
print(max(deposit))