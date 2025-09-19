import os
import json

given = {}
sales_relatory = {}

def save_data():
    with open('given.json', 'w') as f:
        json.dump(given, f, indent= 4)

    with open('sales_relatory.json', 'w') as s:
        json.dump(sales_relatory, s, indent= 4)


def load_data():
    with open('given.json', 'r') as g:
        given = json.load(g)

    with open('sales_relatory.json', 'r') as s:
        sales_relatory = json.load(s)

    return given, sales_relatory

def pause_leave():
    input('Press enter: ')


def remover_product():
    for product in given.keys():
        print(product)

    user_choice = input('what product: ').lower()

    try:
        del given[user_choice]
        del sales_relatory[user_choice]
        print('product removed with sucessfuly')
        save_data()

    except KeyError:
        print('Error, type a valid product')

    finally:
        pause_leave()
    

def sales_report():
    for product, sales in sales_relatory.items():
        print(f'{product}: {sales} sales')
    
    pause_leave()


def register_sale():
    for product in given.keys():
        print(product)
    
    seller_product = input('what product? ').lower()

    try:
        amount_sell = int(input('how many? '))
        given[seller_product][2] -= amount_sell
        
    except KeyError:
        print('Error, type a valid product')

    except ValueError:
        print('Error, type a valid number')

    else:
        print(given)
        sales_relatory[seller_product] = sales_relatory.get(seller_product, 0) + 1
        save_data()

    finally:
        pause_leave()


def lister_product():
    for product, value in given.items():
        print(f'{product}: {value}')
    pause_leave()

    
def register_product():
    while True:        
        name_product = input('type the product name: ').lower()
        if name_product.isdigit() or len(name_product) < 2:
            print('Error, type a valid name product')
            continue

        while True:
            code_product = input('type the product code: ')
            if code_product.isdigit() is False or len(code_product) < 8 or len(code_product) > 13:
                print('Error, type a valid code')
                continue
            break

        given[name_product] = []
        given[name_product].append(code_product)
        
        while True:
            try:
                price_product = float(input('type the product price: '))
                amount_stock_product = int(input('type the amount stock: '))

            except ValueError:
                print('Error, type a valid price like 1.99 not 1,99')
                continue

            else:
                given[name_product].append(price_product)
                given[name_product].append(amount_stock_product)
                print(given)
                break

        leave = input('want to leave[yes/no] ').lower()
        if leave == 'yes':
            print('leaving...')
            pause_leave()
            save_data()
            break
            

def store_menu():
    while True:
        os.system('cls')
        print('-- Menu --')
        print()
        print('1- register product')
        print('2- remove product')
        print('3- list all products')
        print('4- register a sale')
        print('5- sales report')
        print('6- leave')

        user_choice = input('type a option: ')
        if user_choice == '1':
            register_product()

        elif user_choice == '2':
            remover_product()

        elif user_choice == '3':
            lister_product()

        elif user_choice == '4':
            register_sale()

        elif user_choice == '5':
            sales_report()

        elif user_choice == '6':
            print('leaving...')
            break

        else:
            print('Error, choose a valid option')
            input('Press enter: ')

given, sales_relatory = load_data()
store_menu()