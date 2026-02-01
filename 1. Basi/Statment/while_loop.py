# Il ciclo 'while' in Python esegue un blocco di codice fintanto che una condizione specificata è vera.
# È utile quando non si sa in anticipo quante volte si dovrà eseguire il ciclo.

# 1. Esempio base di un ciclo 'while'
# Questo ciclo stamperà i numeri da 1 a 5.
print("Esempio di ciclo while da 1 a 5:")
contatore = 1
while contatore <= 5:
    print(contatore)
    contatore += 1 # È fondamentale modificare la variabile della condizione per evitare un ciclo infinito.

print(f"Valore finale del contatore: {contatore}")


# 2. L'istruzione 'break'
# 'break' può essere usata per uscire da un ciclo 'while' immediatamente.
print("\nUtilizzo di 'break' in un ciclo while:")
contatore = 1
while contatore <= 10:
    if contatore == 5:
        print("Il contatore è 5, esco dal ciclo.")
        break
    print(contatore)
    contatore += 1


# 3. L'istruzione 'continue'
# 'continue' salta il resto del blocco di codice per l'iterazione corrente e torna a controllare la condizione.
print("\nUtilizzo di 'continue' in un ciclo while (stampa solo i numeri dispari):")
contatore = 0
while contatore < 10:
    contatore += 1
    if contatore % 2 == 0: # Se il numero è pari...
        continue # ...salta la print e ricomincia il ciclo.
    print(contatore)


# 4. Il blocco 'else' in un ciclo 'while'
# Simile al ciclo 'for', il blocco 'else' viene eseguito quando la condizione del ciclo 'while' diventa falsa.
# Se il ciclo viene interrotto da un 'break', il blocco 'else' non viene eseguito.
print("\nUtilizzo del blocco 'else' in un ciclo while:")
contatore = 1
while contatore <= 3:
    print(f"Iterazione {contatore}")
    contatore += 1
else:
    print("Il ciclo è terminato perché la condizione è diventata falsa.")

print("\nUtilizzo del blocco 'else' con 'break':")
contatore = 1
while contatore <= 3:
    print(f"Iterazione {contatore}")
    if contatore == 2:
        break
    contatore += 1
else:
    # Questo blocco non viene eseguito.
    print("Questo messaggio non viene stampato.")


# 5. Cicli infiniti (e come gestirli)
# Un ciclo infinito si verifica quando la condizione di un ciclo 'while' rimane sempre vera.
# Spesso sono errori, ma a volte sono usati intenzionalmente con un 'break' per terminarli.
# L'esempio della calcolatrice ('calcolatrice.py') usa un ciclo 'while True' che termina
# solo quando l'utente scrive 'esci'.

# Esempio di ciclo 'while True' per un semplice menu:
# while True:
#     scelta = input("Scrivi 'a' per continuare o 'q' per uscire: ")
#     if scelta.lower() == 'q':
#         print("Uscita in corso...")
#         break
#     elif scelta.lower() == 'a':
#         print("Hai scelto di continuare!")
#     else:
#         print("Scelta non valida.")
# print("Sei uscito dal menu.")
