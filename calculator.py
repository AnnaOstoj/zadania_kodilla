import logging

logging.basicConfig(level = logging.INFO, format='%(asctime)s %(message)s', filename="logfile.log")

task_dict = {1: "Dodawanie", 2: "Odejmowanie", 3: "Mnożenie", 4: "Dzielenie"}

# -- functions -- 

def dodawanie(add_components_float):
    result = 0
    print(f"Dodaję: {add_components_float}")

    for i in add_components_float:
        result += i

    return result
    
def odejmowanie(num_1, num_2):
    print(f"Odejmuję: {num_1} i {num_2}")
    return num_1 - num_2

def mnozenie(add_components_float):
    result = 1
    print(f"Mnożę: {add_components}")

    for i in add_components_float:
        result *= i
    return result

def dzielenie(num_1, num_2):
    if num_2 != 0:
        print(f"Dzielę: {num_1} i {num_2}")
        return num_1 / num_2
    else:
        print("Druga liczba nie może być zerem!")
        return None
        

logging.info(" - - Start programu - - ")
# -- get input data -- 

task = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
if int(task) not in range(5):
    print("To nie jest liczba z przedziału 1 - 4 ")
    logging.warning(f"Podano liczbę {task}, która nie odpowiada żadnemu działaniu matematycznemu")
    exit()
logging.info(f"Wybrano: {task_dict[task]}")

if task == 2 or task == 4:
    while True:
        try:
            num_1 = float(input("Podaj pierwszą liczbę: "))
            num_2 = float(input("Podaj drugą liczbę: "))
            logging.info("Podane liczby są typu float")
            break
        except ValueError:
            print("Oops!  Nieprawidłowa liczba. Spróbuj jeszcze raz!")
            logging.warning("Podana liczba nie jest typu float")

elif task == 1 or task == 3:  
    while True:
        try:
            add_components = input("Podaj dowolną ilość liczb. Rodziel je przecinkami, bez spacji: ").split(",")
            add_components_float = [float(num) for num in add_components]
            logging.info("Podane liczby są typu float")
            break
        except ValueError:
            print("Podaj tylko liczby!")
            logging.warning("Podane liczby nie są typu float")

# -- calculate -- 

if task == 1:
    print("Wynik działania to: {}". format(dodawanie(add_components_float)))
    logging.info(f"Wykonano działanie {task_dict[task]} dla {add_components_float}")
elif task == 2:
    print("Wynik działania to: {}". format(odejmowanie(num_1, num_2)))
    logging.info(f"Wykonano działanie {task_dict[task]} dla {num_1} i {num_2}")
elif task == 3:
    print("Wynik działania to: {}". format(mnozenie(add_components_float)))
    logging.info(f"Wykonano działanie {task_dict[task]} dla {add_components_float}")
elif task == 4:
    result = dzielenie(num_1, num_2)
    if result != None:
        logging.info(f"Wykonano działanie {task_dict[task]} dla {num_1} i {num_2}")
        print("Wynik działania to: {}". format(dzielenie(num_1, num_2)))
    else:
        logging.warning(f"Próbowano podzielić {num_1} przez 0")


logging.info(" - - Koniec programu - - ")
