import math

#Metodo 1 - Funzioni matematiche di base (if statement)
print("\n--- Metodo 1 - Funzioni matematiche di base (if statement) ---")
primoValore=(input("Inserisci il primo valore: "))
secondoValore=(input("Inserisci il secondo valore: "))

#Faccio la conversione a float per permettere operazioni con numeri decimali e non avere errori in caso di divisione
primoValore=float(primoValore)
secondoValore=float(secondoValore)

operazione=input("Inserisci l'operazione (+, -, *, /): ")

if operazione=='+':
    #SOMMA
    risultato=somma(primoValore, secondoValore)
elif operazione=='-':
    #SOTTRAZIONE
    risultato=sottrazione(primoValore, secondoValore)
elif operazione=='*':
    #MOLTIPLICAZIONE
    risultato=moltiplicazione(primoValore, secondoValore)
elif operazione=='/':
    #DIVISIONE
    risultato=divisione(primoValore, secondoValore)
else:
    print("Operazione non valida.")

print(f"Il risultato di {primoValore} / {secondoValore} è {risultato}")

def somma(a, b):
    return a + b
def sottrazione(a, b):
    return a - b
def moltiplicazione(a, b):
    return a * b
def divisione(a, b):
    if b != 0:
        return a / b
    else:
        return "Errore: Divisione per zero non consentita."