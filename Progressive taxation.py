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
