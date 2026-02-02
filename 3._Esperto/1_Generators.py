# I generatori sono un modo efficiente per creare iteratori in Python.
# Permettono di generare valori uno alla volta (lazy evaluation) invece di creare l'intera sequenza in memoria.
# Sono particolarmente utili per lavorare con grandi dataset o sequenze infinite.

# 1. Problema: Liste grandi consumano molta memoria

# Creare una lista di 1 milione di numeri
# lista_grande = [i for i in range(1000000)]  # Occupa molta memoria
# print(f"Lista creata in memoria")


# 2. Soluzione: Generator Expression
# Usa parentesi tonde () invece di quadre []

generatore = (i for i in range(1000000))
print(f"Generatore creato: {generatore}")
print(f"Tipo: {type(generatore)}")

# I valori vengono generati uno alla volta quando richiesti
print(f"Primo valore: {next(generatore)}")
print(f"Secondo valore: {next(generatore)}")
print(f"Terzo valore: {next(generatore)}")


# 3. Funzioni generatrici con yield
# La parola chiave 'yield' trasforma una funzione in un generatore

def conta_fino_a(n):
    """Generatore che conta da 1 a n"""
    i = 1
    while i <= n:
        yield i  # Restituisce il valore e sospende l'esecuzione
        i += 1

print("\n--- Generatore con yield ---")
contatore = conta_fino_a(5)
print(f"Generatore: {contatore}")

# Iterare sul generatore
for numero in contatore:
    print(f"Numero: {numero}")


# 4. Differenza tra return e yield

def funzione_normale():
    """Funzione normale con return"""
    return 1
    return 2  # Questo non viene mai eseguito
    return 3

def funzione_generatore():
    """Funzione generatore con yield"""
    yield 1
    yield 2
    yield 3

print("\n--- Return vs Yield ---")
print(f"Funzione normale: {funzione_normale()}")

print("Funzione generatore:")
for valore in funzione_generatore():
    print(f"  {valore}")


# 5. Generatore per sequenze infinite

def numeri_infiniti():
    """Generatore che produce numeri infiniti"""
    n = 0
    while True:
        yield n
        n += 1

print("\n--- Sequenza infinita ---")
infinito = numeri_infiniti()
print(f"Primi 10 numeri: {[next(infinito) for _ in range(10)]}")


# 6. Generatore di Fibonacci

def fibonacci():
    """Generatore infinito della sequenza di Fibonacci"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print("\n--- Fibonacci ---")
fib = fibonacci()
print("Primi 15 numeri di Fibonacci:")
for i, numero in enumerate(fib):
    if i >= 15:
        break
    print(numero, end=" ")
print()


# 7. Generatore con stato interno

def generatore_con_stato():
    """Generatore che mantiene uno stato interno"""
    print("Inizio del generatore")
    yield 1
    print("Dopo il primo yield")
    yield 2
    print("Dopo il secondo yield")
    yield 3
    print("Fine del generatore")

print("\n--- Stato interno ---")
gen = generatore_con_stato()
print(f"Primo next(): {next(gen)}")
print(f"Secondo next(): {next(gen)}")
print(f"Terzo next(): {next(gen)}")

try:
    next(gen)  # Genera StopIteration
except StopIteration:
    print("Generatore esaurito (StopIteration)")


# 8. Generatore per leggere file grandi
# Invece di caricare tutto il file in memoria

def leggi_file_a_righe(nome_file):
    """Generatore che legge un file riga per riga"""
    try:
        with open(nome_file, 'r') as file:
            for riga in file:
                yield riga.strip()
    except FileNotFoundError:
        print(f"File {nome_file} non trovato")

# Esempio d'uso (commentato perché il file potrebbe non esistere)
# for riga in leggi_file_a_righe('grande_file.txt'):
#     print(riga)


# 9. Generatore con parametri

def ripeti_valore(valore, volte):
    """Generatore che ripete un valore n volte"""
    for _ in range(volte):
        yield valore

print("\n--- Generatore con parametri ---")
for val in ripeti_valore("Python", 3):
    print(val)


# 10. Generatore per filtrare dati

def filtra_pari(numeri):
    """Generatore che filtra solo i numeri pari"""
    for numero in numeri:
        if numero % 2 == 0:
            yield numero

print("\n--- Filtrare numeri pari ---")
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for pari in filtra_pari(numeri):
    print(pari, end=" ")
print()


# 11. Pipeline di generatori
# Combinare più generatori per processare dati in modo efficiente

def numeri_da_1_a_n(n):
    """Genera numeri da 1 a n"""
    for i in range(1, n + 1):
        yield i

def quadrati(numeri):
    """Calcola i quadrati dei numeri"""
    for numero in numeri:
        yield numero ** 2

def solo_pari(numeri):
    """Filtra solo i numeri pari"""
    for numero in numeri:
        if numero % 2 == 0:
            yield numero

print("\n--- Pipeline di generatori ---")
# Creare una pipeline: numeri -> quadrati -> solo pari
pipeline = solo_pari(quadrati(numeri_da_1_a_n(10)))
print(f"Quadrati pari da 1 a 10: {list(pipeline)}")


# 12. Generatore con send()
# I generatori possono ricevere valori durante l'esecuzione

def generatore_interattivo():
    """Generatore che può ricevere valori"""
    print("Generatore avviato")
    while True:
        valore_ricevuto = yield
        print(f"Ricevuto: {valore_ricevuto}")

print("\n--- Generatore con send() ---")
gen = generatore_interattivo()
next(gen)  # Avviare il generatore
gen.send("Ciao")
gen.send("Mondo")
gen.send("Python")


# 13. Generatore bidirezionale

def eco():
    """Generatore che fa eco dei valori ricevuti"""
    while True:
        valore = yield
        if valore is not None:
            yield f"Eco: {valore}"

print("\n--- Generatore bidirezionale ---")
generatore_eco = eco()
next(generatore_eco)  # Inizializzare

generatore_eco.send("Hello")
print(next(generatore_eco))

generatore_eco.send("Python")
print(next(generatore_eco))


# 14. Generatore con yield from
# Delegare a un altro generatore

def generatore_1():
    """Primo generatore"""
    yield 1
    yield 2
    yield 3

def generatore_2():
    """Secondo generatore"""
    yield 4
    yield 5
    yield 6

def generatore_combinato():
    """Combina due generatori usando yield from"""
    yield from generatore_1()
    yield from generatore_2()

print("\n--- yield from ---")
for valore in generatore_combinato():
    print(valore, end=" ")
print()


# 15. Generatore per appiattire liste annidate

def appiattisci(lista):
    """Generatore che appiattisce una lista annidata"""
    for elemento in lista:
        if isinstance(elemento, list):
            yield from appiattisci(elemento)  # Ricorsione
        else:
            yield elemento

print("\n--- Appiattire lista annidata ---")
lista_annidata = [1, [2, 3, [4, 5]], 6, [7, [8, 9]]]
print(f"Lista originale: {lista_annidata}")
print(f"Lista appiattita: {list(appiattisci(lista_annidata))}")


# 16. Generatore per permutazioni

def permutazioni(elementi):
    """Generatore semplice per permutazioni (versione base)"""
    if len(elementi) <= 1:
        yield elementi
    else:
        for i in range(len(elementi)):
            for perm in permutazioni(elementi[:i] + elementi[i+1:]):
                yield [elementi[i]] + perm

print("\n--- Permutazioni ---")
print("Permutazioni di [1, 2, 3]:")
for perm in permutazioni([1, 2, 3]):
    print(perm)


# 17. Generatore per range personalizzato

def range_personalizzato(inizio, fine, passo=1):
    """Generatore che simula range() con float"""
    valore = inizio
    while valore < fine:
        yield valore
        valore += passo

print("\n--- Range personalizzato ---")
print("Range da 0 a 1 con passo 0.1:")
for val in range_personalizzato(0, 1, 0.1):
    print(f"{val:.1f}", end=" ")
print()


# 18. Vantaggi dei generatori

print("\n--- Vantaggi dei generatori ---")

# Memoria: confronto tra lista e generatore
import sys

lista = [i for i in range(10000)]
generatore = (i for i in range(10000))

print(f"Dimensione lista: {sys.getsizeof(lista)} bytes")
print(f"Dimensione generatore: {sys.getsizeof(generatore)} bytes")


# 19. Quando usare i generatori

print("\n--- Quando usare i generatori ---")
print("""
✅ USALI quando:
- Lavori con grandi dataset che non entrano in memoria
- Hai bisogno di sequenze infinite
- Vuoi processare dati in modo lazy (solo quando necessario)
- Stai creando pipeline di trasformazioni dati

❌ NON usarli quando:
- Hai bisogno di accedere agli elementi più volte
- Devi conoscere la lunghezza della sequenza
- Hai bisogno di indicizzazione (es. generatore[5])
- I dati sono piccoli e la semplicità è più importante
""")


# 20. Esempio pratico: Processare log file

def leggi_log(nome_file):
    """Generatore per leggere file di log"""
    try:
        with open(nome_file, 'r') as file:
            for riga in file:
                yield riga.strip()
    except FileNotFoundError:
        print(f"File {nome_file} non trovato")

def filtra_errori(righe):
    """Filtra solo le righe che contengono 'ERROR'"""
    for riga in righe:
        if 'ERROR' in riga:
            yield riga

def estrai_timestamp(righe):
    """Estrae il timestamp dalle righe"""
    for riga in righe:
        # Assumendo formato: [TIMESTAMP] ERROR messaggio
        if riga.startswith('['):
            timestamp = riga[1:riga.index(']')]
            yield timestamp

# Esempio d'uso (commentato)
# pipeline = estrai_timestamp(filtra_errori(leggi_log('app.log')))
# for timestamp in pipeline:
#     print(timestamp)


# 21. Generatore per batch processing

def batch(iterabile, dimensione_batch):
    """Generatore che divide un iterabile in batch di dimensione fissa"""
    batch_corrente = []
    for elemento in iterabile:
        batch_corrente.append(elemento)
        if len(batch_corrente) == dimensione_batch:
            yield batch_corrente
            batch_corrente = []
    if batch_corrente:  # Yield dell'ultimo batch parziale
        yield batch_corrente

print("\n--- Batch processing ---")
numeri = range(1, 13)
for gruppo in batch(numeri, 3):
    print(f"Batch: {gruppo}")


# 22. Generatore con gestione eccezioni

def generatore_con_eccezioni():
    """Generatore che gestisce eccezioni"""
    try:
        yield 1
        yield 2
        yield 3
    except GeneratorExit:
        print("Generatore chiuso prematuramente")
    finally:
        print("Pulizia risorse")

print("\n--- Gestione eccezioni ---")
gen = generatore_con_eccezioni()
print(next(gen))
gen.close()  # Chiude il generatore
