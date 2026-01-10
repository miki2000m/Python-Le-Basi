#La stampa è il primo tipo di approccio a un interfaccia utente in Python.
#In Python, la funzione principale per stampare output è `print()`.
#Questa funzione consente di visualizzare dati sullo schermo o su altri dispositivi

#1. Stampa di una stringa
print("Ciao, mondo!")

#2. Stampa di un numero intero
print(42)

#3. Stampa di un numero decimale
print(3.14)

#4. Stampa di una variabile
nome = "Alice"
print(nome)

#5. Stampa di una variabile con formattazione
eta = 25
print(f"{nome} ha {eta} anni.") # -> questo modo è il MIGLIORE per una stampa formattata

#6. Stampa di più variabili
cognome = "Rossi"
print(f"{nome} {cognome} ha {eta} anni.")

#7. Stampa con separatori personalizzati
print("Python", "è", "divertente", sep=" | ")

#8. Stampa con fine personalizzata
print("Fine della stampa.", end="!\n")

#9. Stampa di una lista
lista = [1, 2, 3, 4, 5]
print("Elementi della lista:", lista)

#10. Stampa di un dizionario
dizionario = {"nome": "Alice", "eta": 25}
print("Dati della persona:", dizionario)

#11. Stampa di un messaggio multilinea
print("""Questo è un messaggio
che si estende su più righe.
È utile per testi lunghi.""")

#12. Stampa di un messaggio con escape characters
print("Questo è un esempio di \"escape character\" per le virgolette.")
