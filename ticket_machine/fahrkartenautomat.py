import json

with open ("tickets.json", "r") as file:
    tickets = json.load(file)

print('Herzlich wilkommen bei ihrer Bahn, sie haben folgende Fahrkarten zur Auswhal:')

for i, ticket in enumerate(tickets["tickets"]):
    print(i, ticket["name"])
    
auswahl = int(input('Bitte geben sie die entsprechende Zahl für die gewünschte Fahrkarte ein: '))

if auswahl >= len(tickets["tickets"]):
    print('Auswahl ist nicht verfügbar bitte neu starten.')
    exit()

ticket_name = tickets["tickets"][auswahl]["name"]    
ticket_price = tickets["tickets"][auswahl]["price"]

print(f'Sie haben das ticket {ticket_name} gewählt. Der Preis beträgt: {ticket_price} Euro.\n')
print('Dieser Automat akzeptiert folgende Münzen und Geldscheine:')
for entry in tickets["accepted_cash"]:
    print(entry, "Euro")

bezahlt = 0
while bezahlt < ticket_price:
    paid = int(input(f'Bitte werfen sie eine Münze/einen Geldschein ein, es fehlen noch {ticket_price - bezahlt} Euro.\n'))
    if paid in tickets['accepted_cash']:
        bezahlt += paid
        print(f'Danke für {paid} Euro.')
    else:
        print('Leider akzeptieren wir diese Münzen/den Geldschein nicht, bitter werfen sie etwas anderes ein.')
print()
if bezahlt > ticket_price:
    print(f'Ihr Restgeld beträgt {bezahlt - ticket_price} Euro.')
print('Danke für ihren Einkauf und gute Fahrt.')
