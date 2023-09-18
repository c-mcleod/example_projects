# Aufgabe 1: Unterschiede zwischen Listen
list1 = [10, 21, 45, 66, 78]
list2 = [10, 22, 46, 66, 78, 90]
sym_differences = set(list1) ^ set(list2)
sd_list = list(sym_differences)
sd_list.sort()
print(sd_list)

# Aufgabe 2: Gemeinsamkeiten von Listen
common_values = set(list1) & set(list2)
common_list = list(common_values)
common_list.sort()
print(common_list)
print()

# Aufgabe 3: Hotel Marrios vs Hotel Hilten
marrios = {
    "name": "Marrios",
    "age": 1999,
    "payment_options": ["card", "cash", "online"],
    "available_rooms": [800, 801, 802, 805, 900, 1000, 1001],
    "price_per_ninght": 50,
    "employees": ["carlo", "maria", "marta", "luis", "fernando"]
}
hilten = {
    "name": "Hilten",
    "age": 1992,
    "payment_options": ["card", "online"],
    "available_rooms": [100, 800, 801, 805, 1000, 1001],
    "price_per_ninght": 70,
    "employees": ["artur", "maria", "oliver", "xenia"]
}
# Frage 1: Du möchtest 5 Nächte im Hotel übernachten.
try:
    nights_stay = int(input("Wie viele Übernachtungen? "))
except ValueError:
    nights_stay = int(input("Wie viele Übernachtungen? Muss eine Nummer sein "))
    
cost_marrios = nights_stay * marrios["price_per_ninght"]
cost_hilten = nights_stay * hilten["price_per_ninght"]
difference = cost_marrios - cost_hilten if cost_marrios > cost_hilten else cost_hilten - cost_marrios
# difference = abs(cost_marrios - cost_hilten)
print(f'{nights_stay} Übernachtungen kosten {cost_marrios}€ im Hotel {marrios["name"]} und {cost_hilten}€ im Hotel {hilten["name"]}. Der Preisunterschied sind {difference}€.')
print()

# Frage 2: Du möchtest gerne deine Anfrage an beide Hotels automatisieren.
#rooms_free = set(marrios["available_rooms"]) ^ set(hilten["available_rooms"])
common_rooms = sorted(set(marrios["available_rooms"]) ^ set(hilten["available_rooms"]))
common_room_numbers = ", ".join(str(room) for room in common_rooms)
print(f'Guten Tag, könnten Sie mir bitte eines der folgenden Zimmer reservieren: {common_room_numbers}? Danke.')
print()

# Frage 3: Lass uns nun die verschiedenen Zahlungsmöglichkeiten verstehen.
# Wie viele verschiedenen Zahlungsmöglichkeiten gibt es im Hotel Marrios und im Hotel Hilten?
print(f'Im Hotel {marrios["name"]} gitb es {len(marrios["payment_options"])} und im Hotel {hilten["name"]} gibt es {len(hilten["payment_options"])} Zahlungsmöglichkeiten.')
print()

# Welche Zahlungsmöglichkeiten gibt es nicht in beiden Hotels?
payment_options = set(marrios["payment_options"]) ^ set(hilten["payment_options"])
print(f'Die Hotels unterscheiden sich in den folgenden Zahlungsmöglichkeiten: {", ".join(payment_options)}.')

# Bonusaufgabe: Dort übernachten, wo Fernando arbeitet.
# Fernando ist ein guter Freund von dir, daher hast du dich entschieden in dem Hotel zu übernachten, wo er als Angestellter eingetragen ist.
worker = str.lower(input('Namen von Freunden finden: '))
def check_worker(worker):
    if worker in marrios["employees"]:
        print(f'Nach der Überprüfung arbeitet {worker.capitalize()} in {marrios["name"]} Hotel und ich werde dort übernachten.')
    elif worker in hilten["employees"]:
        print(f'Nach der Überprüfung arbeitet {worker.capitalize()} in {hilten["name"]} Hotel und ich werde dort übernachten.')
    else:
        print(f'{worker.capitalize()} arbeitet nicht in diesen Hotels.')
check_worker(worker)
