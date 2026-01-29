# I decoratori sono un pattern di design potente in Python che permette di modificare o estendere
# il comportamento di funzioni o classi senza modificarne il codice.
# Sono funzioni che prendono un'altra funzione come input e restituiscono una nuova funzione.

# 1. Concetto base: Funzioni come oggetti
# In Python, le funzioni sono oggetti di prima classe (first-class objects)
# Possono essere assegnate a variabili, passate come argomenti e restituite da altre funzioni

def saluta():
    return "Ciao!"

# Assegnare una funzione a una variabile
funzione_saluto = saluta
print(f"Chiamata tramite variabile: {funzione_saluto()}")


# 2. Funzioni che accettano altre funzioni come parametri

def esegui_due_volte(funzione):
    """Esegue una funzione due volte"""
    funzione()
    funzione()

def stampa_messaggio():
    print("Questo messaggio viene stampato!")

print("\nEseguire una funzione due volte:")
esegui_due_volte(stampa_messaggio)


# 3. Funzioni che restituiscono altre funzioni

def crea_moltiplicatore(n):
    """Crea una funzione che moltiplica per n"""
    def moltiplica(x):
        return x * n
    return moltiplica

# Creare diverse funzioni moltiplicatrici
raddoppia = crea_moltiplicatore(2)
triplica = crea_moltiplicatore(3)

print(f"\nRaddoppia 5: {raddoppia(5)}")
print(f"Triplica 5: {triplica(5)}")


# 4. Il primo decoratore semplice

def mio_decoratore(funzione):
    """Un decoratore base che aggiunge funzionalità prima e dopo la funzione"""
    def wrapper():
        print("--- Inizio esecuzione ---")
        funzione()
        print("--- Fine esecuzione ---")
    return wrapper

# Modo tradizionale di applicare un decoratore
def saluta_mondo():
    print("Ciao, mondo!")

saluta_decorata = mio_decoratore(saluta_mondo)
print("\nChiamata con decoratore (modo tradizionale):")
saluta_decorata()


# 5. Sintassi @ per i decoratori
# Python offre una sintassi più elegante usando @

@mio_decoratore
def saluta_python():
    print("Ciao, Python!")

print("\nChiamata con decoratore (sintassi @):")
saluta_python()


# 6. Decoratori con argomenti
# Per decorare funzioni che accettano parametri, usiamo *args e **kwargs

def decoratore_con_args(funzione):
    def wrapper(*args, **kwargs):
        print(f"Argomenti: {args}, Keyword args: {kwargs}")
        risultato = funzione(*args, **kwargs)
        print(f"Risultato: {risultato}")
        return risultato
    return wrapper

@decoratore_con_args
def somma(a, b):
    return a + b

print("\nFunzione decorata con argomenti:")
somma(5, 3)


# 7. Decoratore per misurare il tempo di esecuzione

import time

def misura_tempo(funzione):
    """Decoratore che misura il tempo di esecuzione di una funzione"""
    def wrapper(*args, **kwargs):
        inizio = time.time()
        risultato = funzione(*args, **kwargs)
        fine = time.time()
        print(f"Tempo di esecuzione di {funzione.__name__}: {fine - inizio:.4f} secondi")
        return risultato
    return wrapper

@misura_tempo
def calcolo_lento():
    """Simula un calcolo che richiede tempo"""
    time.sleep(1)
    return "Calcolo completato"

print("\nMisurazione tempo:")
risultato = calcolo_lento()
print(risultato)


# 8. Decoratore per contare le chiamate

def conta_chiamate(funzione):
    """Decoratore che conta quante volte una funzione viene chiamata"""
    def wrapper(*args, **kwargs):
        wrapper.chiamate += 1
        print(f"Chiamata #{wrapper.chiamate} a {funzione.__name__}")
        return funzione(*args, **kwargs)
    wrapper.chiamate = 0
    return wrapper

@conta_chiamate
def saluta_nome(nome):
    return f"Ciao, {nome}!"

print("\nConteggio chiamate:")
print(saluta_nome("Alice"))
print(saluta_nome("Bob"))
print(saluta_nome("Charlie"))


# 9. Decoratore per il debug

def debug(funzione):
    """Decoratore che stampa informazioni di debug"""
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Chiamata a {funzione.__name__}({signature})")
        risultato = funzione(*args, **kwargs)
        print(f"{funzione.__name__} ha restituito {risultato!r}")
        return risultato
    return wrapper

@debug
def moltiplica(a, b):
    return a * b

print("\nDebug:")
moltiplica(5, 3)


# 10. Decoratori multipli (stacking)
# Si possono applicare più decoratori alla stessa funzione

@debug
@misura_tempo
def operazione_complessa(n):
    """Calcola la somma dei quadrati fino a n"""
    return sum(i**2 for i in range(n))

print("\nDecoratori multipli:")
risultato = operazione_complessa(1000)


# 11. Decoratori con parametri
# Per creare decoratori che accettano parametri, serve un ulteriore livello di nesting

def ripeti(volte):
    """Decoratore che ripete l'esecuzione di una funzione n volte"""
    def decoratore(funzione):
        def wrapper(*args, **kwargs):
            for i in range(volte):
                print(f"Esecuzione {i+1}/{volte}")
                risultato = funzione(*args, **kwargs)
            return risultato
        return wrapper
    return decoratore

@ripeti(volte=3)
def stampa_messaggio_ripetuto(messaggio):
    print(f"  -> {messaggio}")

print("\nDecoratore con parametri:")
stampa_messaggio_ripetuto("Ciao!")


# 12. Preservare i metadati della funzione originale
# Problema: i decoratori sostituiscono i metadati della funzione originale

def decoratore_semplice(funzione):
    def wrapper(*args, **kwargs):
        return funzione(*args, **kwargs)
    return wrapper

@decoratore_semplice
def funzione_esempio():
    """Questa è la docstring della funzione"""
    pass

print(f"\nNome della funzione: {funzione_esempio.__name__}")  # Stampa 'wrapper' invece di 'funzione_esempio'

# Soluzione: usare functools.wraps
from functools import wraps

def decoratore_corretto(funzione):
    @wraps(funzione)  # Preserva i metadati della funzione originale
    def wrapper(*args, **kwargs):
        return funzione(*args, **kwargs)
    return wrapper

@decoratore_corretto
def funzione_corretta():
    """Questa è la docstring corretta"""
    pass

print(f"Nome della funzione corretta: {funzione_corretta.__name__}")


# 13. Decoratori per la validazione degli input

def valida_positivo(funzione):
    """Decoratore che verifica che tutti gli argomenti siano positivi"""
    @wraps(funzione)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Tutti gli argomenti devono essere positivi, ricevuto: {arg}")
        return funzione(*args, **kwargs)
    return wrapper

@valida_positivo
def calcola_area_rettangolo(base, altezza):
    """Calcola l'area di un rettangolo"""
    return base * altezza

print("\nValidazione input:")
print(f"Area (5, 3): {calcola_area_rettangolo(5, 3)}")

try:
    calcola_area_rettangolo(-5, 3)
except ValueError as e:
    print(f"Errore: {e}")


# 14. Decoratore per il caching (memoization)

def cache(funzione):
    """Decoratore che memorizza i risultati delle chiamate precedenti"""
    cache_dati = {}
    
    @wraps(funzione)
    def wrapper(*args):
        if args in cache_dati:
            print(f"Risultato dalla cache per {args}")
            return cache_dati[args]
        print(f"Calcolo per {args}")
        risultato = funzione(*args)
        cache_dati[args] = risultato
        return risultato
    return wrapper

@cache
def fibonacci(n):
    """Calcola l'n-esimo numero di Fibonacci"""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("\nCaching (memoization):")
print(f"Fibonacci(10): {fibonacci(10)}")
print(f"Fibonacci(10) di nuovo: {fibonacci(10)}")  # Usa la cache


# 15. Decoratori di classe
# I decoratori possono essere applicati anche alle classi

def aggiungi_metodo(classe):
    """Decoratore che aggiunge un metodo a una classe"""
    def nuovo_metodo(self):
        return f"Questo è un metodo aggiunto a {self.__class__.__name__}"
    classe.metodo_aggiunto = nuovo_metodo
    return classe

@aggiungi_metodo
class MiaClasse:
    def __init__(self, nome):
        self.nome = nome

oggetto = MiaClasse("Test")
print(f"\nMetodo aggiunto alla classe: {oggetto.metodo_aggiunto()}")


# 16. Decoratori built-in di Python

# @property - Trasforma un metodo in un attributo
class Persona:
    def __init__(self, nome, cognome):
        self._nome = nome
        self._cognome = cognome
    
    @property
    def nome_completo(self):
        """Getter per il nome completo"""
        return f"{self._nome} {self._cognome}"
    
    @nome_completo.setter
    def nome_completo(self, valore):
        """Setter per il nome completo"""
        self._nome, self._cognome = valore.split()

persona = Persona("Mario", "Rossi")
print(f"\n@property - Nome completo: {persona.nome_completo}")
persona.nome_completo = "Luigi Verdi"
print(f"Dopo modifica: {persona.nome_completo}")


# @staticmethod - Metodo che non accede a self o cls
class Matematica:
    @staticmethod
    def somma(a, b):
        """Metodo statico per sommare due numeri"""
        return a + b

print(f"\n@staticmethod - Somma: {Matematica.somma(5, 3)}")


# @classmethod - Metodo che riceve la classe come primo argomento
class Contatore:
    conteggio = 0
    
    @classmethod
    def incrementa(cls):
        """Incrementa il contatore di classe"""
        cls.conteggio += 1
    
    @classmethod
    def ottieni_conteggio(cls):
        """Restituisce il conteggio corrente"""
        return cls.conteggio

Contatore.incrementa()
Contatore.incrementa()
print(f"@classmethod - Conteggio: {Contatore.ottieni_conteggio()}")


# 17. Esempio pratico completo: Sistema di autenticazione

def richiede_autenticazione(funzione):
    """Decoratore che simula un controllo di autenticazione"""
    @wraps(funzione)
    def wrapper(utente, *args, **kwargs):
        if not utente.get("autenticato", False):
            print(f"Accesso negato: utente non autenticato")
            return None
        print(f"Accesso consentito per {utente['nome']}")
        return funzione(utente, *args, **kwargs)
    return wrapper

def richiede_admin(funzione):
    """Decoratore che verifica i permessi di amministratore"""
    @wraps(funzione)
    def wrapper(utente, *args, **kwargs):
        if not utente.get("admin", False):
            print(f"Accesso negato: {utente['nome']} non è amministratore")
            return None
        return funzione(utente, *args, **kwargs)
    return wrapper

@richiede_autenticazione
def visualizza_profilo(utente):
    """Visualizza il profilo utente"""
    return f"Profilo di {utente['nome']}"

@richiede_autenticazione
@richiede_admin
def elimina_utente(utente, id_utente):
    """Elimina un utente (solo admin)"""
    return f"Utente {id_utente} eliminato da {utente['nome']}"

print("\n--- Sistema di autenticazione ---")

# Utente non autenticato
utente_guest = {"nome": "Guest", "autenticato": False}
visualizza_profilo(utente_guest)

# Utente autenticato normale
utente_normale = {"nome": "Alice", "autenticato": True, "admin": False}
print(visualizza_profilo(utente_normale))
elimina_utente(utente_normale, 123)

# Utente amministratore
utente_admin = {"nome": "Admin", "autenticato": True, "admin": True}
print(visualizza_profilo(utente_admin))
print(elimina_utente(utente_admin, 123))
