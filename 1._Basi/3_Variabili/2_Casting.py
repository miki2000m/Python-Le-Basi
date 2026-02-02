#Il casting ci permette di convertire un tipo di dato in un altro.
#Questo è utile quando vogliamo eseguire operazioni tra tipi di dati diversi o quando dobbiamo formattare i dati per l'output.
#In Python, possiamo utilizzare le funzioni `int()`, `float()` e `str()` per effettuare il casting tra i tipi di dati numerici e le stringhe.

#Esempio di casting da int a float
numero_intero = 10
numero_float = float(numero_intero)
print(numero_float)  # Output: 10.0 
#Esempio di casting da float a int
numero_float = 10.5
numero_intero = int(numero_float)
print(numero_intero)  # Output: 10

#Esempio di casting da stringa a int
numero_stringa = "20"
numero_intero = int(numero_stringa)
print(numero_intero)  # Output: 20
#Esempio di casting da int a stringa
numero_intero = 30
numero_stringa = str(numero_intero)
print(numero_stringa)  # Output: "30"

#Esempio di casting da stringa a float
numero_stringa = "15.75"
numero_float = float(numero_stringa)
print(numero_float)  # Output: 15.75
#Esempio di casting da float a stringa
numero_float = 25.5
numero_stringa = str(numero_float)
print(numero_stringa)  # Output: "25.5" 