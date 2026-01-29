# La gestione degli errori, o "Exception Handling", è un meccanismo per gestire gli errori che si verificano durante l'esecuzione di un programma.
# Invece di far crashare il programma, possiamo "catturare" l'errore e decidere come comportarci.
# Si usa il blocco 'try...except'.

# 1. Il blocco 'try...except'
# Il codice che potrebbe generare un errore viene messo nel blocco 'try'.
# Se si verifica un errore, il codice nel blocco 'except' viene eseguito.

print("Esempio di gestione di ZeroDivisionError:")
try:
    risultato = 10 / 0
    print(f"Il risultato è {risultato}") # Questa riga non verrà mai eseguita
except ZeroDivisionError:
    print("Errore: Impossibile dividere per zero!")

print("Il programma continua dopo l'errore.")


# 2. Gestire tipi specifici di errori
# È buona pratica catturare solo gli errori che ci si aspetta di gestire.

print("\nEsempio di gestione di ValueError:")
try:
    numero = int(input("Inserisci un numero intero: "))
    print(f"Hai inserito il numero: {numero}")
except ValueError:
    print("Errore: Non hai inserito un numero intero valido.")


# 3. Gestire più errori
# Si possono avere più blocchi 'except' per gestire diversi tipi di eccezioni.

print("\nEsempio di gestione di più errori:")
try:
    valore = int(input("Inserisci un indice della lista [0, 1, 2]: "))
    lista = [10, 20, 30]
    risultato = lista[valore] / valore
    print(f"Il risultato di lista[{valore}] / {valore} è: {risultato}")
except ValueError:
    print("Input non valido. Devi inserire un numero.")
except IndexError:
    print("Errore: L'indice che hai scelto è fuori dai limiti della lista.")
except ZeroDivisionError:
    print("Errore: Hai scelto l'indice 0, che causa una divisione per zero.")
except Exception as e:
    # 'Exception' è una classe base per quasi tutti gli errori.
    # Catturarla è un modo per gestire qualsiasi altro errore imprevisto.
    # 'as e' assegna l'oggetto eccezione alla variabile 'e', che può essere ispezionata.
    print(f"Si è verificato un errore imprevisto: {e}")


# 4. Il blocco 'else'
# Il blocco 'else' è opzionale e viene eseguito solo se il blocco 'try' non solleva alcuna eccezione.

print("\nEsempio con il blocco 'else':")
try:
    numero = int(input("Inserisci un numero intero (diverso da zero): "))
    risultato = 100 / numero
except ValueError:
    print("Input non valido.")
except ZeroDivisionError:
    print("Non puoi dividere per zero.")
else:
    # Questo codice viene eseguito solo se non ci sono stati errori.
    print(f"Il risultato della divisione è: {risultato}")


# 5. Il blocco 'finally'
# Il blocco 'finally' è opzionale e viene SEMPRE eseguito, indipendentemente dal fatto che si sia verificato un errore o meno.
# È utile per le operazioni di "pulizia", come chiudere una connessione a un database o un file.

print("\nEsempio con il blocco 'finally':")
f = None
try:
    # L'istruzione 'with' è generalmente preferita per i file perché gestisce questo automaticamente,
    # ma usiamo l'approccio manuale per dimostrare 'finally'.
    f = open("Python Le Basi/Errori/test_finally.txt", 'w')
    f.write("test")
    # Simuliamo un errore dopo l'apertura del file
    # 10 / 0
    print("File scritto con successo.")
except IOError:
    print("Errore durante la scrittura del file.")
finally:
    print("Esecuzione del blocco 'finally'.")
    if f is not None:
        f.close()
        print("File chiuso.")


# 6. Sollevare un'eccezione ('raise')
# È possibile sollevare manualmente un'eccezione usando la parola chiave 'raise'.
# Questo è utile per segnalare che qualcosa è andato storto secondo la logica del tuo programma.

def calcola_area_rettangolo(larghezza, altezza):
    if larghezza < 0 or altezza < 0:
        # I valori negativi non sono ammessi per dimensioni fisiche.
        raise ValueError("Larghezza e altezza devono essere numeri non negativi.")
    return larghezza * altezza

try:
    area = calcola_area_rettangolo(10, -5)
    print(f"Area: {area}")
except ValueError as e:
    print(f"\nErrore nella funzione: {e}")
