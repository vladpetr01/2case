type_family = input('Выберите тип семьи:\n1.один 2.пара 3. одиночка')
JAN = 'Январе'
FAB = 'Феврале'
MAR = 'Марте'
APR = 'Апреле'
MAY = 'Мае'
JUN = 'Июне'
JUL = 'Июле'
AUG = 'Августе'
SEP = 'Сентябре'
OCT = 'Октябре'
NOV = 'Ноябре'
DEC = 'Декабре'
name_month = [JAN, FAB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC]
annual_income = 0
for month in range(12):
    print('{} {}:'.format('СКОЛЬКО ТЫ ЗАРАБОТАЛ В' , name_month[month], end = ''))
    income = float(input())
    annual_income += income
if type_family == '1':
    if 0 < annual_income <= 9075:
        tax = 0.1 * annual_income
    elif 9076 <= annual_income <= 36900:
        tax = 0.1 * 9075 + 0.15 * (annual_income - 9075)
    elif 36901 <= annual_income <= 89350:
        tax = 0.1 * 9075 + 0.15 * (36900 - 9075) + 0.25 * (annual_income - 36900)
print(tax)