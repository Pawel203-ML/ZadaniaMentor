#Kalkulator
import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')



if __name__ == "__main__":
    type_operation = input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ')
    first_number = input('Podaj pierwsza liczbe: ')
    second_number = input('Podaj druga liczbe: ')

    
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