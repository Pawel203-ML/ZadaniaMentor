#Kalkulator
import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')


#funkcja pobiera dane listy i sprawdza czy kazdy jej element jest konwertowalny na int
def IsConvertable(numbers):
    try:
        for number in numbers:
            float(number)
    except:
        logging.error('Znaleziono slowo, uzyj tylko liczb')

def TypeEquasion(value1):
    try:
        if 0 < float(value1) < 5:
            return True
        else:
            logging.error('Liczba spoza zakresu, Spruboj ponownie')
    except:
        logging.error('Niepoprawna komenda, Sprobuj podac liczbe z zakresu')

numbers = []

if __name__ == "__main__":
    while True:
        result = 1.0
        while True:
            type_operation = input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ')
            if TypeEquasion(type_operation) == True:
                break
        if int(type_operation) == 3:
            while True:
                while True:
                    logging.info('Podaj liczby oddzielone przecinkiem!')
                    numbers = input('Podaj liczby: ').split(',')
                    if IsConvertable(numbers) == None:
                        break
                try:
                    numbers = list(map(float, numbers)) #dziala
                    iter_numbers = iter(numbers)
                    break
                except:
                    logging.error('Nieprawidlowo wprowadzone dane, sprubuj ponownie')

            while True:
                try:
                    multi_numbers = lambda x, y: x * y
                    result = multi_numbers(result, next(iter_numbers))
                except:
                    break
            logging.info(f'Mnoze liczby: {numbers}')
            logging.info(f'Wynik to: {result}')

        elif int(type_operation) == 1:
            while True:
                logging.info('Podaj liczby oddzielone przecinkiem!')
                numbers = input('Podaj liczby: ').split(',')
                if IsConvertable(numbers) == None:
                    break
            numbers = list(map(float, numbers)) #dziala
            result = sum(numbers)
            logging.info(f'Dodaje liczby: {numbers}')
            logging.info(f'Wynik to: {result}')

        else:
            while True:
                while True:
                    numbers.append(input('Podaj pierwsza liczbe: '))
                    numbers.append(input('Podaj druga liczbe: '))
                    if IsConvertable(numbers) == None:
                        break
            
                if int(type_operation) == 4:
                    try:
                        result = float(numbers[0]) / float(numbers[1])
                        logging.info(f'Dziele: {numbers[0]}, {numbers[1]}')
                        logging.info(f'Wynik to: {result}')
                        break
                    except:
                        logging.error('Nie mozna dzielic przez zero!')
                elif int(type_operation) == 2:
                    result = float(numbers[0]) - float(numbers[1])
                    logging.info(f'Odejmuje: {numbers[0]}, {numbers[1]}')
                    logging.info(f'Wynik to: {result}')
                    break
                numbers = []
        while True:
            answer = input('Czy chcesz liczyc dalej? T/N: ')
            if answer == 'T' or answer == 't':
                break
            elif answer == 'N' or answer == 'n':
                exit()
            else:
                logging.info('Sprawdz pisownie')
