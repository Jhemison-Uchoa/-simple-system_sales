def validator_cpf():
    while True:
        user_cpf = input('type your cpf: ')
        if len(user_cpf) == 11 and user_cpf.isdigit() and user_cpf != user_cpf[0] * 11:
            peso_resultado = 0
            peso_multiplicador = 10

            for number_digit in (user_cpf[:9]):
                peso_resultado += int(number_digit) * peso_multiplicador
                peso_multiplicador -= 1

            peso_resultado = (peso_resultado * 10) % 11
            result = 0 if peso_resultado > 9 else peso_resultado

            peso_resultado_2 = 0
            peso_multiplicador_2 = 11

            for number_digit_2 in user_cpf[:10]:
                peso_resultado_2 += int(number_digit_2) * peso_multiplicador_2
                peso_multiplicador_2 -= 1
            
            peso_resultado_2 = (peso_resultado_2 * 10) % 11
            result_2 = 0 if peso_resultado_2 > 9 else peso_resultado_2

            if str(result) == user_cpf[9] and str(result_2) == user_cpf[10]:
                print('CPF VALID, you can pass')

            else:
                print('CPF INVALID, stop here')

            leave = input('want leave?[yes/no] ').lower()
            if leave == 'yes':
                print('leaving...')
                break

        elif len(user_cpf) != 11:
            print('Error, type a valid 11 digits cpf')
            continue

        else:
            print('Error, type only numbers, like : 14343212393, not 143.432.123-93')
            print('not like example: 11111111111, error too')

from datetime import datetime

def age_legal():
    while True:
        year_actually = datetime.now().year

        try: 
            year_user = int(input('what year your born? '))
            year_size = len(str(year_user))
            if year_actually - year_user >= 18 and year_size == 4 and year_user >= 1925:
                print(f'you have {year_actually - year_user} years old, you is adult')

            elif year_size != 4:
                print('Error, type a valid 4-digit year')
                continue

            elif year_user <= 1924 or year_user > year_actually:
                print('Error, impossible, type a valid number please!')
                continue

            else:
                print(f'you have {year_actually - year_user} years old, you is kid')

            leave = input('want leave? [yes/no] ').lower()
            if leave == 'yes':
                print('leaving...')
                break

        except ValueError:
            print('Error, type a valid number')
            continue

def convert_currency():
    print('this program will convert real to dolar and reverse') 
    while True:
        try:
            number = float(input('type number to convert: '))
            print('1 - [Dolar -> real]')
            print('2 - [Real -> dolar]')
            coin = input('choose a option: ')

            if coin == '1':
                print(f'{number * 5.41:,.2f} BRL')

            elif coin == '2':
                print(f'{number * 0.18:,.2f} USD')

            else:
                print('Error, choose a valid option')
                continue

            leave = input('want leave? [yes/no] ').lower()
            if leave == 'yes':
                print('leaving...')
                break
                
        except ValueError:
            print('Error, type a valid number')
            continue

def options():
    while True:
        print('--Main Menu--')
        print('1 - convert real/dolar')
        print('2 - validate legal age')
        print('3 - validate cpf')
        print('4 - leave')
        choice = input('choose a option above: ')
        if choice == '1':
            convert_currency()

        elif choice == '2':
            age_legal()

        elif choice == '3':
            validator_cpf()
          
        elif choice == '4':
            print('leaving program...')
            break

options()