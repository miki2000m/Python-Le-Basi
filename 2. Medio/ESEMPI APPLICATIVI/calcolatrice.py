# Una calcolatrice di base in Python
# Questo esempio dimostra l'uso di funzioni, input/output, e gestione degli errori di base.

# Definiamo le funzioni per le operazioni matematiche prima di utilizzarle.
# Questo è fondamentale in Python, altrimenti il programma non saprà cosa sono 'somma', 'sottrazione', etc.

def somma(a, b):
    """Questa funzione esegue l'addizione di due numeri."""
    return a + b

def sottrazione(a, b):
    """Questa funzione esegue la sottrazione di due numeri."""
    return a - b

def moltiplicazione(a, b):
    """Questa funzione esegue la moltiplicazione di due numeri."""
    return a * b

def divisione(a, b):
    """
    Questa funzione esegue la divisione di due numeri.
    Include un controllo per evitare la divisione per zero.
    """
    if b != 0:
        return a / b
    else:
        # È buona pratica gestire i casi anomali e ritornare un messaggio di errore.
        return "Errore: Divisione per zero non consentita."

# Utilizziamo un ciclo 'while True' per far sì che la calcolatrice continui a funzionare
# finché l'utente non decide di uscire.
while True:
    print("\n--- Calcolatrice Python ---")
    print("Operazioni disponibili: +, -, *, /")
    print("Scrivi 'esci' per terminare il programma.")

    # Chiediamo all'utente di inserire l'operazione
    operazione = input("Inserisci l'operazione (+, -, *, /) o 'esci': ")

    # Controlliamo se l'utente vuole uscire
    if operazione.lower() == 'esci':
        print("Grazie per aver usato la calcolatrice. Arrivederci!")
        break  # Interrompe il ciclo while

    # Verifichiamo che l'operazione sia una di quelle valide
    if operazione in ['+', '-', '*', '/']:
        # Usiamo un blocco try-except per gestire il caso in cui l'utente inserisca un valore non numerico
        try:
            primoValore = float(input("Inserisci il primo valore: "))
            secondoValore = float(input("Inserisci il secondo valore: "))
        except ValueError:
            print("Errore: per favore, inserisci solo numeri per i valori.")
            continue # Salta il resto del ciclo e ricomincia

        risultato = None  # Inizializziamo il risultato a None
        
        # Eseguiamo l'operazione corretta in base alla scelta
        if operazione == '+':
            risultato = somma(primoValore, secondoValore)
        elif operazione == '-':
            risultato = sottrazione(primoValore, secondoValore)
        elif operazione == '*':
            risultato = moltiplicazione(primoValore, secondoValore)
        elif operazione == '/':
            risultato = divisione(primoValore, secondoValore)

        # Stampiamo il risultato in modo corretto e generico
        # Questo risolve l'errore precedente dove stampava sempre il messaggio della divisione
        if isinstance(risultato, str): # Se il risultato è una stringa, è un messaggio di errore
            print(risultato)
        else:
            print(f"Il risultato di {primoValore} {operazione} {secondoValore} è {risultato}")

    else:
        print("Operazione non valida. Per favore, scegli tra '+', '-', '*', '/'.")