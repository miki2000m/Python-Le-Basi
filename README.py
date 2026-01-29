# GUIDA COMPLETA PYTHON - INDICE
# Questa è una guida di riferimento rapido per tutti i file di esempio Python

"""
===========================================
PYTHON - DALLE BASI ALLE PARTI AVANZATE
===========================================

Questa collezione di file copre tutti gli aspetti fondamentali e avanzati di Python,
dalle basi della programmazione fino ai concetti più complessi.

STRUTTURA DELLA GUIDA:
"""

print("""
╔════════════════════════════════════════════════════════════════════╗
║                    FONDAMENTI DI PYTHON                            ║
╚════════════════════════════════════════════════════════════════════╝

1. VARIABILI E TIPI DI DATI
   📁 Variabili/Variabili.py
   - Tipi di base: int, float, string, boolean
   - Dichiarazione e assegnamento
   - Convenzioni di naming

   📁 Variabili/Casting.py
   - Conversione tra tipi di dati
   - int(), float(), str()
   - Gestione errori di casting

   📁 Variabili/StringMethods.py ⭐ COMPLETO
   - Tutti i metodi delle stringhe
   - Manipolazione, ricerca, formattazione
   - Validazione e pulizia testo
   - Slicing e concatenazione

2. INPUT E OUTPUT
   📁 Input.py
   - Ricevere input dall'utente
   - Conversione tipi di input
   - Validazione input

   📁 Stampa.py
   - Funzione print()
   - Formattazione output
   - f-strings e .format()

3. OPERAZIONI MATEMATICHE
   📁 Math.py
   - Operazioni base (+, -, *, /)
   - Modulo math
   - Funzioni matematiche avanzate
   - Costanti (pi, e)


╔════════════════════════════════════════════════════════════════════╗
║                    STRUTTURE DI CONTROLLO                          ║
╚════════════════════════════════════════════════════════════════════╝

4. CONDIZIONI E DECISIONI
   📁 Statment/if.py
   - if, elif, else
   - Operatori di confronto
   - Condizioni annidate

   📁 Statment/Operatori.py
   - Operatori logici (and, or, not)
   - Operatori di confronto
   - Operatori di identità e appartenenza

   📁 Statment/conditional expressions.py
   - Espressioni condizionali inline
   - Operatore ternario

5. CICLI E ITERAZIONI
   📁 Statment/for_loop.py
   - Ciclo for
   - range()
   - Iterazione su sequenze

   📁 Statment/while_loop.py
   - Ciclo while
   - break e continue
   - Loop infiniti


╔════════════════════════════════════════════════════════════════════╗
║                    STRUTTURE DATI                                  ║
╚════════════════════════════════════════════════════════════════════╝

6. COLLEZIONI
   📁 Strutture Dati/List.py
   - Liste: creazione, accesso, modifica
   - Metodi: append, insert, remove, pop
   - Slicing e list comprehension

   📁 Strutture Dati/Tuple.py
   - Tuple: immutabili
   - Unpacking
   - Quando usare tuple vs liste

   📁 Strutture Dati/Dictionary.py
   - Dizionari: chiave-valore
   - Metodi: get, keys, values, items
   - Dictionary comprehension

   📁 Strutture Dati/Set.py
   - Set: collezioni uniche
   - Operazioni su set
   - Set comprehension


╔════════════════════════════════════════════════════════════════════╗
║                    FUNZIONI E MODULARITÀ                           ║
╚════════════════════════════════════════════════════════════════════╝

7. FUNZIONI
   📁 Funzioni/Funzioni.py
   - Definizione e chiamata
   - Parametri e argomenti
   - Return values
   - *args e **kwargs
   - Scope delle variabili

   📁 Lambda.py ⭐ NUOVO
   - Funzioni lambda (anonime)
   - map(), filter(), reduce()
   - Funzioni di ordine superiore
   - sorted() con lambda

8. MODULI
   📁 Modules/mymodule.py
   - Creare moduli personalizzati
   - Import e from...import

   📁 Modules/main.py
   - Usare moduli
   - __name__ == "__main__"


╔════════════════════════════════════════════════════════════════════╗
║              PROGRAMMAZIONE ORIENTATA AGLI OGGETTI                 ║
╚════════════════════════════════════════════════════════════════════╝

9. CLASSI E OGGETTI
   📁 OOP/Classi.py
   - Definire classi
   - __init__ (costruttore)
   - Attributi e metodi
   - self
   - __str__ e metodi speciali

   📁 OOP/Ereditarieta.py
   - Ereditarietà
   - super()
   - Polimorfismo
   - Metodi override


╔════════════════════════════════════════════════════════════════════╗
║                    GESTIONE ERRORI E FILE                          ║
╚════════════════════════════════════════════════════════════════════╝

10. GESTIONE ECCEZIONI
    📁 Errori/try_except.py
    - try, except, finally
    - Tipi di eccezioni
    - raise
    - Creare eccezioni personalizzate

11. FILE HANDLING
    📁 File Handling/file_handling.py
    - Aprire e chiudere file
    - Leggere e scrivere
    - with statement
    - Modalità di apertura


╔════════════════════════════════════════════════════════════════════╗
║                    CONCETTI AVANZATI                               ║
╚════════════════════════════════════════════════════════════════════╝

12. COMPREHENSIONS ⭐ NUOVO
    📁 Comprehensions.py
    - List comprehensions
    - Dictionary comprehensions
    - Set comprehensions
    - Generator expressions
    - Quando usarle e quando evitarle

13. GENERATORI ⭐ NUOVO
    📁 Generators.py
    - Funzioni generatrici con yield
    - Lazy evaluation
    - Generatori infiniti
    - yield from
    - Pipeline di generatori
    - Vantaggi di memoria

14. DECORATORI ⭐ NUOVO
    📁 Decorators.py
    - Concetto di decoratore
    - Sintassi @decorator
    - Decoratori con argomenti
    - functools.wraps
    - @property, @staticmethod, @classmethod
    - Decoratori pratici (timing, caching, validazione)

15. CONTEXT MANAGERS ⭐ NUOVO
    📁 ContextManagers.py
    - Pattern with
    - __enter__ e __exit__
    - @contextmanager
    - Gestione risorse
    - ExitStack
    - Esempi pratici (file, database, lock)

16. ESPRESSIONI REGOLARI ⭐ NUOVO
    📁 RegularExpressions.py
    - Modulo re
    - Pattern matching
    - Metacaratteri e classi
    - Gruppi e cattura
    - Validazioni (email, telefono, password)
    - Cheat sheet regex

17. PROGRAMMAZIONE ASINCRONA ⭐ NUOVO
    📁 AsyncAwait.py
    - async e await
    - asyncio
    - Task e coroutine
    - asyncio.gather()
    - Timeout e gestione errori
    - Queue, Lock, Semaphore asincroni
    - Quando usare async


╔════════════════════════════════════════════════════════════════════╗
║                    ESEMPI APPLICATIVI                              ║
╚════════════════════════════════════════════════════════════════════╝

18. PROGETTI PRATICI
    📁 ESEMPI APPLICATIVI/calcolatrice.py
    - Applicazione completa
    - Integrazione di concetti


╔════════════════════════════════════════════════════════════════════╗
║                    PERCORSO DI APPRENDIMENTO                       ║
╚════════════════════════════════════════════════════════════════════╝

LIVELLO PRINCIPIANTE (1-2 settimane):
1. Variabili/Variabili.py
2. Stampa.py
3. Input.py
4. Math.py
5. Statment/if.py
6. Statment/for_loop.py
7. Statment/while_loop.py

LIVELLO INTERMEDIO (2-3 settimane):
8. Strutture Dati/List.py
9. Strutture Dati/Dictionary.py
10. Funzioni/Funzioni.py
11. Variabili/StringMethods.py
12. Errori/try_except.py
13. File Handling/file_handling.py
14. OOP/Classi.py

LIVELLO AVANZATO (3-4 settimane):
15. Lambda.py
16. Comprehensions.py
17. Generators.py
18. Decorators.py
19. ContextManagers.py
20. RegularExpressions.py
21. AsyncAwait.py
22. OOP/Ereditarieta.py


╔════════════════════════════════════════════════════════════════════╗
║                    SUGGERIMENTI PER LO STUDIO                      ║
╚════════════════════════════════════════════════════════════════════╝

📚 COME USARE QUESTA GUIDA:

1. LEGGI IL CODICE
   - Ogni file contiene commenti dettagliati
   - Gli esempi sono progressivi (dal semplice al complesso)

2. ESEGUI GLI ESEMPI
   - Esegui ogni file con: python nome_file.py
   - Sperimenta modificando i valori
   - Osserva l'output

3. PRATICA
   - Prova a scrivere variazioni degli esempi
   - Combina concetti da file diversi
   - Crea i tuoi progetti

4. RIFERIMENTO RAPIDO
   - Usa questo file come indice
   - Cerca argomenti specifici
   - Rivedi concetti quando necessario


╔════════════════════════════════════════════════════════════════════╗
║                    RISORSE AGGIUNTIVE                              ║
╚════════════════════════════════════════════════════════════════════╝

📖 DOCUMENTAZIONE UFFICIALE:
   https://docs.python.org/3/

🎓 TUTORIAL INTERATTIVI:
   https://www.learnpython.org/
   https://realpython.com/

🔧 STRUMENTI UTILI:
   - Python REPL (interprete interattivo)
   - IPython (REPL avanzato)
   - Jupyter Notebook (per sperimentare)

🧪 TESTING REGEX:
   https://regex101.com/


╔════════════════════════════════════════════════════════════════════╗
║                    PROSSIMI PASSI                                  ║
╚════════════════════════════════════════════════════════════════════╝

Dopo aver completato questa guida, considera di approfondire:

🚀 FRAMEWORK E LIBRERIE:
   - Django / Flask (web development)
   - NumPy / Pandas (data science)
   - Matplotlib / Seaborn (visualizzazione)
   - TensorFlow / PyTorch (machine learning)
   - FastAPI (API moderne)

🎯 BEST PRACTICES:
   - PEP 8 (style guide)
   - Type hints
   - Testing (unittest, pytest)
   - Virtual environments
   - Package management (pip, poetry)

💻 PROGETTI PRATICI:
   - Web scraper
   - API REST
   - Bot Telegram/Discord
   - Analisi dati
   - Automazione task


╔════════════════════════════════════════════════════════════════════╗
║                    BUONO STUDIO! 🐍                                ║
╚════════════════════════════════════════════════════════════════════╝
""")

# Statistiche della guida
print("\n" + "="*70)
print("STATISTICHE DELLA GUIDA")
print("="*70)

import os

# Conta i file Python nella directory
directory = os.path.dirname(os.path.abspath(__file__))
file_python = [f for f in os.listdir(directory) if f.endswith('.py')]

print(f"📊 File di esempio: {len(file_python)}")
print(f"📁 Directory principale: {directory}")
print(f"✨ Nuovi file aggiunti: 7")
print(f"   - Comprehensions.py")
print(f"   - Lambda.py")
print(f"   - Generators.py")
print(f"   - Decorators.py")
print(f"   - ContextManagers.py")
print(f"   - RegularExpressions.py")
print(f"   - AsyncAwait.py")
print(f"🔧 File aggiornati: 1")
print(f"   - Variabili/StringMethods.py (espanso da 8 a 228 righe)")

print("\n" + "="*70)
print("Inizia il tuo viaggio in Python! 🚀")
print("="*70)
