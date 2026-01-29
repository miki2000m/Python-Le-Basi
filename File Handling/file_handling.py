# La gestione dei file (File Handling) è una parte cruciale della programmazione.
# Python fornisce funzioni semplici per creare, leggere, aggiornare ed eliminare file.

# Il modo raccomandato per lavorare con i file è usare l'istruzione 'with'.
# 'with' gestisce automaticamente la chiusura del file, anche se si verificano errori.

# 1. Scrivere su un file ('w' - write mode)
# La modalità 'w' crea un nuovo file per la scrittura.
# ATTENZIONE: Se il file esiste già, il suo contenuto verrà CANCELLATO.
file_path = "Python Le Basi/File Handling/esempio.txt"

print(f"Scrivendo nel file: {file_path}")
try:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("Ciao, mondo dei file!\n")
        f.write("Questa è la seconda riga.\n")
        f.write("I caratteri speciali come à, è, ì sono gestiti correttamente grazie a encoding='utf-8'.\n")
    print("Scrittura completata.")
except IOError as e:
    print(f"Si è verificato un errore di I/O: {e}")


# 2. Leggere un file ('r' - read mode)
# La modalità 'r' è usata per leggere il contenuto di un file. È la modalità di default.
print(f"\nLeggendo l'intero contenuto del file:")
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        contenuto = f.read() # Legge l'intero file in una singola stringa
        print("--- Inizio Contenuto ---")
        print(contenuto)
        print("--- Fine Contenuto ---")
except FileNotFoundError:
    print(f"Errore: Il file {file_path} non è stato trovato.")
except IOError as e:
    print(f"Si è verificato un errore di I/O: {e}")


# 3. Aggiungere contenuto a un file ('a' - append mode)
# La modalità 'a' apre il file per aggiungere contenuto alla fine.
# Se il file non esiste, viene creato.
print(f"\nAggiungendo contenuto al file (append):")
try:
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write("Questa riga viene aggiunta alla fine del file.\n")
    print("Contenuto aggiunto.")
except IOError as e:
    print(f"Si è verificato un errore di I/O: {e}")

# Rileggiamo per vedere la differenza
print("\nRileggendo il file dopo l'append:")
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        print(f.read())
except FileNotFoundError:
    print(f"Errore: Il file {file_path} non è stato trovato.")


# 4. Leggere un file riga per riga
# Questo è un approccio efficiente per file di grandi dimensioni, poiché non carica tutto in memoria.
print("\nLeggendo il file riga per riga:")
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        for riga in f:
            print(f"Riga letta: {riga.strip()}") # .strip() rimuove spazi bianchi e newline iniziali/finali
except FileNotFoundError:
    print(f"Errore: Il file {file_path} non è stato trovato.")

# In alternativa, usando readlines() per ottenere una lista di righe
print("\nLeggendo il file con readlines():")
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        righe = f.readlines()
        print(righe)
except FileNotFoundError:
    print(f"Errore: Il file {file_path} non è stato trovato.")


# 5. Eliminare un file
# Per eliminare un file, è necessario importare il modulo 'os'.
import os

# Prima di eliminare, è buona norma controllare se il file esiste.
if os.path.exists(file_path):
    # os.remove(file_path)
    # print(f"\nFile '{file_path}' eliminato con successo.")
    # Decommenta la riga sopra per eseguire l'eliminazione del file.
    # Per ora lo lasciamo per poter rieseguire lo script.
    print(f"\nIl file '{file_path}' potrebbe essere eliminato (codice commentato).")
else:
    print(f"\nIl file '{file_path}' non esiste, quindi non può essere eliminato.")

# Altre modalità utili:
# 'r+': Lettura e scrittura. Apre il file per leggere e scrivere. Il puntatore è all'inizio.
# 'w+': Scrittura e lettura. Crea/tronca il file e lo apre per scrivere e leggere.
# 'a+': Aggiunta e lettura. Apre il file per aggiungere e leggere. Il puntatore è alla fine.
# 'b': Modalità binaria (es. 'rb', 'wb'). Usata per file non di testo, come immagini o audio.
