# Il Context Manager è un pattern che permette di gestire risorse in modo sicuro,
# garantendo che vengano sempre rilasciate correttamente, anche in caso di errori.
# Il modo più comune è usare l'istruzione 'with'.

# 1. Problema: Gestione manuale delle risorse

# Modo tradizionale (rischioso)
print("--- Gestione manuale (senza with) ---")
file = open('esempio.txt', 'w')
try:
    file.write('Contenuto del file')
finally:
    file.close()  # Dobbiamo ricordarci di chiudere il file
    print("File chiuso manualmente")


# 2. Soluzione: Context Manager con 'with'

print("\n--- Context Manager (con with) ---")
# Il file viene chiuso automaticamente alla fine del blocco with
with open('esempio.txt', 'w') as file:
    file.write('Contenuto del file con context manager')
# Il file è già chiuso qui
print("File chiuso automaticamente")


# 3. Vantaggi del Context Manager

print("\n--- Vantaggi ---")
print("""
✅ Garantisce il rilascio delle risorse anche in caso di eccezioni
✅ Codice più pulito e leggibile
✅ Previene memory leaks e file descriptor leaks
✅ Segue il principio RAII (Resource Acquisition Is Initialization)
""")


# 4. Context Manager con file multipli

print("--- File multipli ---")
with open('file1.txt', 'w') as f1, open('file2.txt', 'w') as f2:
    f1.write('Contenuto file 1')
    f2.write('Contenuto file 2')
print("Entrambi i file chiusi automaticamente")


# 5. Creare un Context Manager con una classe
# Deve implementare i metodi __enter__ e __exit__

class MioContextManager:
    """Context manager personalizzato"""
    
    def __init__(self, nome):
        self.nome = nome
        print(f"Inizializzazione: {self.nome}")
    
    def __enter__(self):
        """Chiamato all'inizio del blocco with"""
        print(f"Entrata nel context: {self.nome}")
        return self  # Questo viene assegnato alla variabile dopo 'as'
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Chiamato alla fine del blocco with (anche in caso di eccezioni)"""
        print(f"Uscita dal context: {self.nome}")
        if exc_type is not None:
            print(f"Eccezione catturata: {exc_type.__name__}: {exc_value}")
        # Return False per propagare l'eccezione, True per sopprimerla
        return False

print("\n--- Context Manager personalizzato ---")
with MioContextManager("Test") as cm:
    print(f"Dentro il blocco with")
    print(f"Oggetto context manager: {cm.nome}")


# 6. Context Manager che gestisce eccezioni

print("\n--- Gestione eccezioni ---")
try:
    with MioContextManager("Con eccezione") as cm:
        print("Prima dell'eccezione")
        raise ValueError("Errore di test")
        print("Questa riga non viene eseguita")
except ValueError as e:
    print(f"Eccezione gestita esternamente: {e}")


# 7. Context Manager con contextlib
# Modo più semplice usando il decoratore @contextmanager

from contextlib import contextmanager

@contextmanager
def mio_context_semplice(nome):
    """Context manager creato con contextlib"""
    # Codice di setup (equivalente a __enter__)
    print(f"Setup: {nome}")
    try:
        yield nome  # Questo valore viene restituito al blocco with
    finally:
        # Codice di cleanup (equivalente a __exit__)
        print(f"Cleanup: {nome}")

print("\n--- Context Manager con @contextmanager ---")
with mio_context_semplice("Test contextlib") as valore:
    print(f"Valore ricevuto: {valore}")


# 8. Context Manager per misurare il tempo

import time

@contextmanager
def timer(nome):
    """Context manager per misurare il tempo di esecuzione"""
    print(f"Inizio timer: {nome}")
    inizio = time.time()
    try:
        yield
    finally:
        fine = time.time()
        print(f"Fine timer: {nome} - Tempo: {fine - inizio:.4f} secondi")

print("\n--- Timer ---")
with timer("Operazione lenta"):
    time.sleep(0.5)
    print("Operazione in corso...")


# 9. Context Manager per gestire connessioni database (simulato)

class DatabaseConnection:
    """Simula una connessione a un database"""
    
    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False
    
    def __enter__(self):
        print(f"Connessione al database: {self.db_name}")
        self.connected = True
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Chiusura connessione al database: {self.db_name}")
        self.connected = False
        return False
    
    def query(self, sql):
        if not self.connected:
            raise Exception("Database non connesso")
        print(f"Esecuzione query: {sql}")
        return ["risultato1", "risultato2"]

print("\n--- Connessione database ---")
with DatabaseConnection("mydb") as db:
    risultati = db.query("SELECT * FROM users")
    print(f"Risultati: {risultati}")


# 10. Context Manager per lock (threading)

import threading

class Lock:
    """Context manager per gestire lock"""
    
    def __init__(self, nome):
        self.nome = nome
        self.lock = threading.Lock()
    
    def __enter__(self):
        print(f"Acquisizione lock: {self.nome}")
        self.lock.acquire()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Rilascio lock: {self.nome}")
        self.lock.release()
        return False

print("\n--- Lock ---")
with Lock("risorsa_condivisa"):
    print("Sezione critica - accesso esclusivo")


# 11. Context Manager per cambiare directory

import os

@contextmanager
def cambia_directory(path):
    """Context manager per cambiare temporaneamente directory"""
    directory_originale = os.getcwd()
    print(f"Directory corrente: {directory_originale}")
    try:
        os.chdir(path)
        print(f"Cambiato in: {os.getcwd()}")
        yield
    finally:
        os.chdir(directory_originale)
        print(f"Ritornato a: {directory_originale}")

print("\n--- Cambio directory ---")
try:
    with cambia_directory('/tmp'):
        print("Operazioni nella directory temporanea")
except Exception as e:
    print(f"Errore: {e}")


# 12. Context Manager per sopprimere eccezioni

from contextlib import suppress

print("\n--- Soppressione eccezioni ---")

# Senza suppress
try:
    int('non_un_numero')
except ValueError:
    pass  # Ignora l'errore

# Con suppress (più pulito)
with suppress(ValueError):
    int('non_un_numero')
print("Eccezione soppressa con suppress()")


# 13. Context Manager per redirect output

from contextlib import redirect_stdout
import io

print("\n--- Redirect output ---")
f = io.StringIO()
with redirect_stdout(f):
    print("Questo viene scritto nel buffer")
    print("Non appare nella console")

output = f.getvalue()
print(f"Output catturato: {output}")


# 14. Context Manager annidati

@contextmanager
def risorsa(nome):
    """Context manager per simulare una risorsa"""
    print(f"  Apertura risorsa: {nome}")
    try:
        yield nome
    finally:
        print(f"  Chiusura risorsa: {nome}")

print("\n--- Context Manager annidati ---")
with risorsa("A"):
    with risorsa("B"):
        with risorsa("C"):
            print("  Tutte le risorse aperte")


# 15. Context Manager con ExitStack
# Gestire un numero dinamico di context manager

from contextlib import ExitStack

print("\n--- ExitStack ---")
with ExitStack() as stack:
    # Aggiungere context manager dinamicamente
    files = [stack.enter_context(open(f'file{i}.txt', 'w')) for i in range(3)]
    
    for i, f in enumerate(files):
        f.write(f'Contenuto file {i}')
    
    print("Tutti i file aperti")
# Tutti i file vengono chiusi automaticamente


# 16. Context Manager per gestire variabili temporanee

@contextmanager
def variabile_temporanea(dizionario, chiave, valore_temp):
    """Imposta temporaneamente un valore in un dizionario"""
    valore_originale = dizionario.get(chiave)
    dizionario[chiave] = valore_temp
    print(f"Valore temporaneo impostato: {chiave} = {valore_temp}")
    try:
        yield
    finally:
        if valore_originale is not None:
            dizionario[chiave] = valore_originale
        else:
            dizionario.pop(chiave, None)
        print(f"Valore ripristinato")

print("\n--- Variabile temporanea ---")
config = {"debug": False}
print(f"Config iniziale: {config}")

with variabile_temporanea(config, "debug", True):
    print(f"Config durante with: {config}")

print(f"Config finale: {config}")


# 17. Context Manager per transazioni (simulato)

class Transaction:
    """Simula una transazione database"""
    
    def __init__(self, nome):
        self.nome = nome
        self.committed = False
    
    def __enter__(self):
        print(f"Inizio transazione: {self.nome}")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            self.commit()
        else:
            self.rollback()
        return False  # Propaga l'eccezione
    
    def commit(self):
        print(f"COMMIT transazione: {self.nome}")
        self.committed = True
    
    def rollback(self):
        print(f"ROLLBACK transazione: {self.nome}")
        self.committed = False

print("\n--- Transazione con successo ---")
with Transaction("tx1") as tx:
    print("Operazione 1")
    print("Operazione 2")

print("\n--- Transazione con errore ---")
try:
    with Transaction("tx2") as tx:
        print("Operazione 1")
        raise Exception("Errore durante la transazione")
        print("Questa operazione non viene eseguita")
except Exception as e:
    print(f"Eccezione: {e}")


# 18. Esempio pratico: Logger con context manager

@contextmanager
def log_operazione(nome_operazione):
    """Context manager per loggare inizio e fine di un'operazione"""
    print(f"[LOG] Inizio: {nome_operazione}")
    inizio = time.time()
    try:
        yield
    except Exception as e:
        print(f"[ERROR] {nome_operazione} fallita: {e}")
        raise
    else:
        durata = time.time() - inizio
        print(f"[LOG] Fine: {nome_operazione} (durata: {durata:.4f}s)")

print("\n--- Logger ---")
with log_operazione("Calcolo complesso"):
    time.sleep(0.2)
    risultato = sum(i**2 for i in range(1000))
    print(f"Risultato: {risultato}")


# 19. Context Manager per gestire stato

class StatoApplicazione:
    """Context manager per gestire lo stato dell'applicazione"""
    
    def __init__(self):
        self.stato = "inattivo"
    
    @contextmanager
    def modalita_manutenzione(self):
        """Entra in modalità manutenzione temporaneamente"""
        stato_precedente = self.stato
        self.stato = "manutenzione"
        print(f"Stato cambiato: {stato_precedente} -> {self.stato}")
        try:
            yield
        finally:
            self.stato = stato_precedente
            print(f"Stato ripristinato: {self.stato}")

print("\n--- Gestione stato ---")
app = StatoApplicazione()
app.stato = "attivo"
print(f"Stato iniziale: {app.stato}")

with app.modalita_manutenzione():
    print(f"Durante manutenzione: {app.stato}")

print(f"Stato finale: {app.stato}")


# 20. Best practices

print("\n--- Best Practices ---")
print("""
✅ Usa 'with' per gestire risorse (file, connessioni, lock)
✅ Implementa sempre __exit__ per rilasciare risorse
✅ Usa @contextmanager per context manager semplici
✅ Gestisci le eccezioni appropriatamente in __exit__
✅ Documenta cosa fa il context manager

❌ Non usare context manager per logica che non riguarda risorse
❌ Non sopprimere eccezioni senza una buona ragione
❌ Non dimenticare il blocco finally in @contextmanager
""")
