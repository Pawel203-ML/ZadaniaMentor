#Kalkulator
import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')


#funkcja pobiera dane listy i sprawdza czy kazdy jej element jest konwertowalny na int
def IsConvertable(numbers):
    try:
        for number in numbers:
            int(number)
    except:
        logging.error('Znaleziono slowo, uzyj tylko liczb')

def TypeEquasion(value1):
    try:
        if 0 < int(value1) < 5:
            return True
        else:
            logging.error('Liczba spoza zakresu, Spruboj ponownie')
    except:
        logging.error('Niepoprawna komenda, Sprobuj podac liczbe z zakresu')

numbers = []
result = 1

if __name__ == "__main__":
    while True:
        type_operation = input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ')
        if TypeEquasion(type_operation) == True:
            break
    if int(type_operation) == 3:
        while True:
            logging.info('Podaj liczby oddzielone przecinkiem!')
            numbers = input('Podaj liczby: ').split(',')
            if IsConvertable(numbers) == None:
                break
        numbers = list(map(int, numbers)) #dziala
        iter_numbers = iter(numbers)
        while True:
            try:
                multi_numbers = lambda x, y: x * y
                result = multi_numbers(result, next(iter_numbers))
            except:
                break
        logging.info(f'Wynik to: {result}')

    elif int(type_operation) == 1:
        while True:
            logging.info('Podaj liczby oddzielone przecinkiem!')
            numbers = input('Podaj liczby: ').split(',')
            if IsConvertable(numbers) == None:
                break
        numbers = list(map(int, numbers)) #dziala
        result = sum(numbers)
        logging.info(f'Wynik to: {result}')

    else:
        while True:
            numbers.append(input('Podaj pierwsza liczbe: '))
            numbers.append(input('Podaj druga liczbe: '))
            if IsConvertable(numbers) == None:
                break
    
        if int(type_operation) == 4:
            result = int(numbers[0]) / int(numbers[1])
            logging.info(f'Dziele: {numbers[0]}, {numbers[1]}')
            logging.info(f'Wynik to: {result}')
        elif int(type_operation) == 2:
            result = int(numbers[0]) - int(numbers[1])
            logging.info(f'Odejmuje: {numbers[0]}, {numbers[1]}')
            logging.info(f'Wynik to: {result}')
