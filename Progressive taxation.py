#Case-study №2
#Developers:   Mauter A. (50%)
#              Kuzmin E. (40%)
#              Petrov V. (50%)
import rulocal as ru

#Which family type.
print(ru.choice_type_family, '\n 1.', ru.type_family_1, '2.', ru.type_family_2, '3.', ru.type_family_3)
type_family = input()

#Write the salary for the all mounth.
JAN = ru.January
FAB = ru.February
MAR = ru.March
APR = ru.April
MAY = ru.May
JUN = ru.June
JUL = ru.July
AUG = ru.August
SEP = ru.September
OCT = ru.October
NOV = ru.November
DEC = ru.December
name_month = [JAN, FAB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC]
annual_income = 0
for month in range(12):
    print('{} {}:'.format(ru.Question, name_month[month], end=''))
    income = float(input())
    annual_income += income
  
#Tax for the single people.
if type_family == '1':
    if 0 < annual_income <= 9075:
        tax = 0.1 * annual_income
    elif 9076 <= annual_income <= 36900:
        tax = 0.1 * 9075 + 0.15 * (annual_income - 9075)
    elif 36901 <= annual_income <= 89350:
        tax = 0.1 * 9075 + 0.15 * (36900 - 9075) + 0.25 * (annual_income - 36900)
    elif 89351 <= annual_income <= 186350:
        tax = 0.1 * 9075 + 0.15 * (36900 - 9075) + 0.25 * (89350 - 36900) + 0.28 * (annual_income - 89350)
    elif 186351 <= annual_income <= 405100:
        tax = 0.1 * 9075 + 0.15 * (36900 - 9075) + 0.25 * (89350 - 36900) + 0.28 * (186350 - 89350) + \
              0.33 * (annual_income - 186350)
    elif 405101 <= annual_income <= 406750:
        tax = 0.1 * 9075 + 0.15 * (36900 - 9075) + 0.25 * (89350 - 36900) + 0.28 * (186350 - 89350) + \
              0.33 * (405100 - 186350) + 0.35 * (annual_income - 405100)
    elif 406751 <= annual_income:
        tax = 0.1 * 9075 + 0.15 * (36900 - 9075) + 0.25 * (89350 - 36900) + 0.28 * (186350 - 89350) + \
              0.33 * (405100 - 186350) + 0.35 * (406750 - 405100) + 0.396 * (annual_income - 406750)
        
#Tax for the married.
elif type_family == '2':
    if 0 < annual_income <= 18150:
        tax = 0.1 * annual_income
    elif 18151 <= annual_income <= 73800:
        tax = 0.1 * 18150 + 0.15 * (annual_income - 18150)
    elif 73801 <= annual_income <= 148850:
        tax = 0.1 * 18150 + 0.15 * (73800 - 18150) + 0.25 * (annual_income - 73800)
    elif 148851 <= annual_income <= 226850:
        tax = 0.1 * 18150 + 0.15 * (73800 - 18150) + 0.25 * (148850 - 73800) + 0.28 * (annual_income - 148850)
    elif 226851 <= annual_income <= 405100:
        tax = 0.1 * 18150 + 0.15 * (73800 - 18150) + 0.25 * (148850 - 73800) + 0.28 * (226850 - 148850) + \
              0.33 * (annual_income - 186350)
    elif 405101 <= annual_income <= 457600:
        tax = 0.1 * 18150 + 0.15 * (73800 - 18150) + 0.25 * (148850 - 73800) + 0.28 * (226850 - 148850) + \
              0.33 * (405100 - 226850) + 0.35 * (annual_income - 405100)
    elif 457600 <= annual_income:
        tax = 0.1 * 18150 + 0.15 * (73800 - 18150) + 0.25 * (148850 - 73800) + 0.28 * (226850 - 148850) + \
              0.33 * (405100 - 226850) + 0.35 * (457600 - 405100) + 0.396 * (annual_income - 457600)

#Tax for the single parrent.
elif type_family == '3':
    if 0 < annual_income <= 12950:
        tax = 0.1 * annual_income
    elif 12950 <= annual_income <= 49400:
        tax = 0.1 * 12950 + 0.15 * (annual_income - 12950)
    elif 49401 <= annual_income <= 127500:
        tax = 0.1 * 12950 + 0.15 * (49400 - 12950) + 0.25 * (annual_income - 49400)
    elif 127501 <= annual_income <= 206600:
        tax = 0.1 * 12950 + 0.15 * (49400 - 12950) + 0.25 * (127550 - 49400) + 0.28 * (annual_income - 127550)
    elif 206601 <= annual_income <= 405100:
        tax = 0.1 * 12950 + 0.15 * (49400 - 12950) + 0.25 * (127550 - 49400) + 0.28 * (206600 - 127550) + \
              0.33 * (annual_income - 206600)
    elif 405101 <= annual_income <= 432200:
        tax = 0.1 * 12950 + 0.15 * (49400 - 12950) + 0.25 * (127550 - 49400) + 0.28 * (206600 - 127550) + \
              0.33 * (405100 - 206600) + 0.35 * (annual_income - 405100)
    elif 432201 <= annual_income:
        tax = 0.1 * 12950 + 0.15 * (49400 - 12950) + 0.25 * (127550 - 49400) + 0.28 * (206600 - 127550) + \
              0.33 * (405100 - 206600) + 0.35 * (432200 - 405100) + 0.396 * (annual_income - 432200)
print(ru.The_amount_of_tax_will_be, tax, '$')
