#Gli operatori logici sono la base di informatici e programmatori per prendere decisioni nei loro programmi.
#Essi permettono di combinare più condizioni booleane (True o False) per creare espressioni più complesse.
#E in oltre questi operatori logici sono la base di qualsiasi struttura informatica sia hardware che software.
#Gli operatori logici più comuni in Python sono: AND, OR, NOT

#Operatore AND
#L'operatore AND restituisce True solo se entrambe le condizioni sono True.
print("\n--- Operatore AND ---")
temp=25
if temp>20 and temp<30:
    print(f"La temperatura di {temp}°C è piacevole.")
elif temp<=20 and temp>=10:
    print(f"La temperatura di {temp}°C è fresca.")
elif temp<10:
    print(f"La temperatura di {temp}°C è fredda.")
else:
    print(f"La temperatura di {temp}°C è calda.")

#Operatore OR
#L'operatore OR restituisce True se almeno una delle condizioni è True.
print("\n--- Operatore OR ---")
giorno="Sabato"
if giorno=="Sabato" or giorno=="Domenica":
    print(f"Oggi è {giorno}, è il fine settimana!")
else:
    print(f"Oggi è {giorno}, è un giorno feriale.")

#Operatore NOT
#L'operatore NOT inverte il valore booleano di una condizione.
print("\n--- Operatore NOT ---")
piove=False
if not piove:
    print("Non sta piovendo, puoi uscire senza ombrello.")
else:
    print("Sta piovendo, prendi un ombrello.")