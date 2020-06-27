import logging

logging.basicConfig(level = logging.INFO, format='%(asctime)s %(message)s', filename="logfile.log")

# -- functions -- 

def dodawanie(numbers_float):
    result = 0
    print(f"Dodaję: {numbers_float}")

    for i in numbers_float:
        result += i

    return result
    
def odejmowanie(numbers_float):

    print(f"Odejmuję: {numbers_float}")
    return numbers_float[0] -  numbers_float[1]

def mnozenie(numbers_float):
    result = 1
    print(f"Mnożę: {numbers_float}")

    for i in numbers_float:
        result *= i
    return result

def dzielenie(numbers_float):
    if numbers_float[1] != 0:
        print(f"Dzielę: {numbers_float}")
        return numbers_float[0] /  numbers_float[1]
    else:
        print("Druga liczba nie może być zerem!")
        return None
        
def get_data(task):

    if task == 2 or task == 4:
        while True:
            try:
                num_1 = float(input("Podaj pierwszą liczbę: "))
                num_2 = float(input("Podaj drugą liczbę: "))
                logging.info("Podane liczby są typu float")
                return [num_1, num_2]
                break
            except ValueError:
                print("Oops!  Nieprawidłowa liczba. Spróbuj jeszcze raz!")
                logging.warning("Podana liczba nie jest typu float")

    elif task == 1 or task == 3:  
        while True:
            try:
                numbers = input("Podaj dowolną ilość liczb. Rodziel je przecinkami, bez spacji: ").split(",")
                numbers_float = [float(num) for num in numbers]
                logging.info("Podane liczby są typu float")
                return numbers_float
                break
            except ValueError:
                print("Podaj tylko liczby!")
                logging.warning("Podane liczby nie są typu float")


task_dict = {1: dodawanie, 2: odejmowanie, 3: mnozenie, 4: dzielenie}

logging.info(" - - Start programu - - ")

# get function type

task = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
if int(task) not in range(5):
    print("To nie jest liczba z przedziału 1 - 4 ")
    logging.warning(f"Podano liczbę {task}, która nie odpowiada żadnemu działaniu matematycznemu")
    exit()
logging.info(f"Wybrano: {task_dict[task]}")

# get input for function

data = get_data(task)

result = task_dict[task](data)

print("Wynik działania to: {}". format(result))
logging.info(f"Wykonano działanie {task_dict[task]} dla {data}")

logging.info(" - - Koniec programu - - ")
