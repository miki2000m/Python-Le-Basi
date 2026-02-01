# GUIDA COMPLETA PYTHON - ORGANIZZATA PER LIVELLO
# Tutti gli esempi sono ora suddivisi in tre livelli di difficoltà

"""
═══════════════════════════════════════════════════════════════════════
    PYTHON - DALLE BASI ALLE PARTI AVANZATE
    Organizzato per Livello di Difficoltà
═══════════════════════════════════════════════════════════════════════

Gli esempi sono ora organizzati in tre cartelle principali:
📁 1. Basi      - Fondamenti di Python (principianti)
📁 2. Medio     - Concetti intermedi
📁 3. Esperto   - Concetti avanzati
"""

print("""
╔════════════════════════════════════════════════════════════════════╗
║                    📁 1. BASI (PRINCIPIANTI)                       ║
╚════════════════════════════════════════════════════════════════════╝

TEMPO STIMATO: 1-2 settimane
PREREQUISITI: Nessuno

📂 Variabili/
   ├── Variabili.py          - Tipi di base (int, float, string, bool)
   ├── Casting.py            - Conversione tra tipi
   └── StringMethods.py      - Tutti i metodi delle stringhe

📄 Input.py                  - Ricevere input dall'utente
📄 Stampa.py                 - Output e formattazione
📄 Math.py                   - Operazioni matematiche

📂 Statment/
   ├── if.py                 - Condizioni (if, elif, else)
   ├── Operatori.py          - Operatori logici e di confronto
   ├── conditional expressions.py - Espressioni ternarie
   ├── for_loop.py           - Ciclo for e iterazioni
   └── while_loop.py         - Ciclo while

📂 Strutture Dati/
   ├── List.py               - Liste e metodi
   ├── Tuple.py              - Tuple (immutabili)
   ├── Dictionary.py         - Dizionari chiave-valore
   └── Set.py                - Set (collezioni uniche)

📂 Funzioni/
   └── Funzioni.py           - Definizione, parametri, return, *args, **kwargs

📂 Modules/
   ├── mymodule.py           - Creare moduli
   └── main.py               - Usare moduli

📂 OOP/
   ├── Classi.py             - Classi, oggetti, __init__, metodi
   └── Ereditarieta.py       - Ereditarietà e polimorfismo

📂 Errori/
   └── try_except.py         - Gestione eccezioni

📂 File Handling/
   └── file_handling.py      - Leggere e scrivere file


╔════════════════════════════════════════════════════════════════════╗
║                    📁 2. MEDIO (INTERMEDIO)                        ║
╚════════════════════════════════════════════════════════════════════╝

TEMPO STIMATO: 2-3 settimane
PREREQUISITI: Completare "1. Basi"

📄 Lambda.py                 - Funzioni lambda e funzioni di ordine superiore
                              (map, filter, reduce, sorted con lambda)

📄 Comprehensions.py         - List/Dict/Set comprehensions
                              Generator expressions

📂 ESEMPI APPLICATIVI/
   └── calcolatrice.py       - Progetto completo che integra i concetti


╔════════════════════════════════════════════════════════════════════╗
║                    📁 3. ESPERTO (AVANZATO)                        ║
╚════════════════════════════════════════════════════════════════════╝

TEMPO STIMATO: 3-4 settimane
PREREQUISITI: Completare "1. Basi" e "2. Medio"

📄 Generators.py             - Generatori con yield, lazy evaluation
                              Pipeline di generatori, generatori infiniti

📄 Decorators.py             - Pattern decoratore, @decorator
                              Decoratori con argomenti, @property
                              Timing, caching, validazione

📄 ContextManagers.py        - Pattern with, __enter__/__exit__
                              @contextmanager, gestione risorse
                              File, database, lock, transazioni

📄 RegularExpressions.py     - Modulo re, pattern matching
                              Validazioni (email, telefono, password)
                              Metacaratteri, gruppi, cheat sheet

📄 AsyncAwait.py             - Programmazione asincrona
                              async/await, asyncio, Task
                              Queue, Lock, Semaphore asincroni


╔════════════════════════════════════════════════════════════════════╗
║                    🎯 PERCORSO DI APPRENDIMENTO                    ║
╚════════════════════════════════════════════════════════════════════╝

SETTIMANA 1-2: BASI
┌─────────────────────────────────────────────────────────────────┐
│ Giorno 1-2:   Variabili, Input, Stampa, Math                    │
│ Giorno 3-4:   if, for_loop, while_loop                          │
│ Giorno 5-7:   List, Dictionary, Tuple, Set                      │
│ Giorno 8-10:  Funzioni, Modules                                 │
│ Giorno 11-14: OOP (Classi, Ereditarietà), Errori, File          │
└─────────────────────────────────────────────────────────────────┘

SETTIMANA 3-4: MEDIO
┌─────────────────────────────────────────────────────────────────┐
│ Giorno 1-3:   Lambda (map, filter, reduce)                      │
│ Giorno 4-7:   Comprehensions (list, dict, set)                  │
│ Giorno 8-14:  Progetto pratico (calcolatrice + progetti propri) │
└─────────────────────────────────────────────────────────────────┘

SETTIMANA 5-8: ESPERTO
┌─────────────────────────────────────────────────────────────────┐
│ Giorno 1-5:   Generators (yield, pipeline)                      │
│ Giorno 6-10:  Decorators (timing, caching)                      │
│ Giorno 11-15: ContextManagers (with, risorse)                   │
│ Giorno 16-20: RegularExpressions (validazioni)                  │
│ Giorno 21-28: AsyncAwait (programmazione asincrona)             │
└─────────────────────────────────────────────────────────────────┘


╔════════════════════════════════════════════════════════════════════╗
║                    📚 COME STUDIARE                                ║
╚════════════════════════════════════════════════════════════════════╝

1️⃣  INIZIA DALLA CARTELLA "1. Basi"
    - Non saltare argomenti
    - Ogni concetto si basa sul precedente
    - Pratica con ogni file prima di passare al successivo

2️⃣  ESEGUI OGNI ESEMPIO
    cd "/Users/michel/Desktop/programmazione/PYTHON/Python Le Basi/1. Basi"
    python Input.py

3️⃣  MODIFICA E SPERIMENTA
    - Cambia i valori
    - Prova variazioni
    - Rompi il codice per capire gli errori

4️⃣  CREA I TUOI PROGETTI
    - Dopo ogni sezione, crea qualcosa di tuo
    - Combina concetti diversi
    - Risolvi problemi reali

5️⃣  PASSA AL LIVELLO SUCCESSIVO
    - Solo quando ti senti sicuro
    - Rivedi i concetti se necessario
    - Non avere fretta


╔════════════════════════════════════════════════════════════════════╗
║                    ✅ CHECKLIST DI PROGRESSO                       ║
╚════════════════════════════════════════════════════════════════════╝

BASI (Fondamentali):
□ Variabili e tipi di dati
□ Input e output
□ Operazioni matematiche
□ Condizioni (if/else)
□ Cicli (for/while)
□ Liste e dizionari
□ Funzioni
□ Classi e OOP
□ Gestione errori
□ File handling

MEDIO (Intermedio):
□ Funzioni lambda
□ map(), filter(), reduce()
□ List comprehensions
□ Dictionary comprehensions
□ Progetto pratico completato

ESPERTO (Avanzato):
□ Generatori e yield
□ Decoratori
□ Context managers
□ Espressioni regolari
□ Programmazione asincrona


╔════════════════════════════════════════════════════════════════════╗
║                    🎓 CERTIFICAZIONE DI COMPETENZA                 ║
╚════════════════════════════════════════════════════════════════════╝

Quando completi ogni livello, crea un progetto che dimostri le tue competenze:

📌 PROGETTO BASI:
   - Gestionale semplice (es. rubrica telefonica)
   - Usa: variabili, liste/dict, funzioni, file, try/except

📌 PROGETTO MEDIO:
   - Analizzatore di dati (es. statistiche da file CSV)
   - Usa: comprehensions, lambda, map/filter

📌 PROGETTO ESPERTO:
   - Web scraper asincrono con validazione
   - Usa: async/await, regex, decorators, context managers


╔════════════════════════════════════════════════════════════════════╗
║                    🔗 RISORSE UTILI                                ║
╚════════════════════════════════════════════════════════════════════╝

📖 Documentazione Ufficiale:
   https://docs.python.org/3/

🎮 Esercizi Interattivi:
   https://www.learnpython.org/
   https://exercism.org/tracks/python

🧪 Testing Regex:
   https://regex101.com/

💬 Community:
   https://stackoverflow.com/questions/tagged/python
   https://www.reddit.com/r/learnpython/


╔════════════════════════════════════════════════════════════════════╗
║                    🚀 PROSSIMI PASSI                               ║
╚════════════════════════════════════════════════════════════════════╝

Dopo aver completato tutti e tre i livelli, considera:

🌐 WEB DEVELOPMENT:
   - Django (framework completo)
   - Flask (micro-framework)
   - FastAPI (API moderne)

📊 DATA SCIENCE:
   - NumPy (calcolo numerico)
   - Pandas (analisi dati)
   - Matplotlib/Seaborn (visualizzazione)

🤖 MACHINE LEARNING:
   - Scikit-learn (ML classico)
   - TensorFlow/PyTorch (deep learning)

🔧 AUTOMAZIONE:
   - Selenium (web automation)
   - BeautifulSoup (web scraping)
   - Requests (HTTP)

📱 DESKTOP/MOBILE:
   - Tkinter/PyQt (GUI desktop)
   - Kivy (mobile apps)


╔════════════════════════════════════════════════════════════════════╗
║                    💡 CONSIGLI FINALI                              ║
╚════════════════════════════════════════════════════════════════════╝

✨ La pratica è più importante della teoria
✨ Sbagliare è parte del processo di apprendimento
✨ Leggi il codice di altri programmatori
✨ Contribuisci a progetti open source
✨ Costruisci un portfolio di progetti
✨ Non smettere mai di imparare

═══════════════════════════════════════════════════════════════════════
                    BUONO STUDIO! 🐍
═══════════════════════════════════════════════════════════════════════
""")

# Statistiche
print("\n" + "="*70)
print("📊 STATISTICHE DELLA GUIDA")
print("="*70)
print(f"📁 Livello Basi:    12 file/cartelle")
print(f"📁 Livello Medio:    3 file/cartelle")
print(f"📁 Livello Esperto:  5 file")
print(f"📝 Totale esempi:   20+ file Python")
print(f"⏱️  Tempo totale stimato: 6-9 settimane")
print("="*70)
print("\n🎯 Inizia dalla cartella '1. Basi' e procedi in ordine!")
print("="*70)
