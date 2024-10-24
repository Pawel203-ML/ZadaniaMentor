#Kalkulator
import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def ifConvertable(value1, value2):
    try:
        int(value1)
        int(value2)
    except:
        logging.error('Znaleziono slowo, Wprowadz same liczby')

def TypeEquasion(value1):
    if 0 < int(value1) < 5:
        return True
    else:
        logging.error('Liczba spoza zakresu, Spruboj ponownie')

if __name__ == "__main__":
    while True:
        type_operation = input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ')
        if TypeEquasion(type_operation) == True:
            break
    while True:
        first_number = input('Podaj pierwsza liczbe: ')
        second_number = input('Podaj druga liczbe: ')
        if ifConvertable(first_number, second_number) == None:
            break
    
    if type_operation == '1':
        result = int(first_number) + int(second_number)
        logging.info(f'Dodaje: {first_number}, {second_number}')
        logging.info(f'Wynik to: {result}')
    elif type_operation == '2':
        result = int(first_number) - int(second_number)
        logging.info(f'Odejmuje: {first_number}, {second_number}')
        logging.info(f'Wynik to: {result}')
    elif type_operation == '3':
        result = int(first_number) * int(second_number)
        logging.info(f'Mnoze: {first_number}, {second_number}')
        logging.info(f'Wynik to: {result}')
    else:
        result = int(first_number) / int(second_number)
        logging.info(f'Dziele: {first_number}, {second_number}')
        logging.info(f'Wynik to: {result}')