# La programmazione asincrona permette di eseguire operazioni senza bloccare il programma.
# È particolarmente utile per operazioni I/O (rete, file, database) che richiedono tempo di attesa.
# Python usa async/await per la programmazione asincrona.

import asyncio
import time

# 1. Confronto tra codice sincrono e asincrono

print("--- Codice Sincrono vs Asincrono ---")

# Codice sincrono (bloccante)
def operazione_lenta_sync(nome, secondi):
    """Simula un'operazione che richiede tempo (sincrona)"""
    print(f"[SYNC] Inizio {nome}")
    time.sleep(secondi)  # Blocca l'esecuzione
    print(f"[SYNC] Fine {nome}")
    return f"Risultato di {nome}"

print("\nEsecuzione sincrona:")
inizio = time.time()
risultato1 = operazione_lenta_sync("Operazione 1", 2)
risultato2 = operazione_lenta_sync("Operazione 2", 2)
fine = time.time()
print(f"Tempo totale sincrono: {fine - inizio:.2f} secondi")


# Codice asincrono (non bloccante)
async def operazione_lenta_async(nome, secondi):
    """Simula un'operazione che richiede tempo (asincrona)"""
    print(f"[ASYNC] Inizio {nome}")
    await asyncio.sleep(secondi)  # Non blocca, permette ad altre operazioni di eseguire
    print(f"[ASYNC] Fine {nome}")
    return f"Risultato di {nome}"

async def esegui_async():
    """Esegue operazioni asincrone in parallelo"""
    inizio = time.time()
    # Eseguire entrambe le operazioni contemporaneamente
    risultati = await asyncio.gather(
        operazione_lenta_async("Operazione 1", 2),
        operazione_lenta_async("Operazione 2", 2)
    )
    fine = time.time()
    print(f"Tempo totale asincrono: {fine - inizio:.2f} secondi")
    return risultati

print("\nEsecuzione asincrona:")
# asyncio.run() esegue la funzione asincrona
risultati = asyncio.run(esegui_async())


# 2. Sintassi base: async e await

print("\n--- Sintassi Base ---")

async def saluta_async():
    """Funzione asincrona semplice"""
    print("Ciao!")
    await asyncio.sleep(1)  # Aspetta 1 secondo senza bloccare
    print("Come stai?")
    return "Saluto completato"

# Eseguire una funzione asincrona
risultato = asyncio.run(saluta_async())
print(f"Risultato: {risultato}")


# 3. Creare e gestire Task

print("\n--- Task ---")

async def task_esempio(nome, durata):
    """Task che simula un'operazione"""
    print(f"Task {nome} iniziato")
    await asyncio.sleep(durata)
    print(f"Task {nome} completato")
    return f"Risultato {nome}"

async def gestisci_task():
    """Crea e gestisce multipli task"""
    # Creare task
    task1 = asyncio.create_task(task_esempio("A", 2))
    task2 = asyncio.create_task(task_esempio("B", 1))
    task3 = asyncio.create_task(task_esempio("C", 3))
    
    # Aspettare che tutti i task completino
    risultati = await asyncio.gather(task1, task2, task3)
    return risultati

risultati = asyncio.run(gestisci_task())
print(f"Risultati: {risultati}")


# 4. asyncio.gather() - Eseguire multipli coroutine

print("\n--- asyncio.gather() ---")

async def scarica_file(nome, dimensione):
    """Simula il download di un file"""
    print(f"Inizio download: {nome}")
    await asyncio.sleep(dimensione / 10)  # Simula tempo di download
    print(f"Download completato: {nome}")
    return f"{nome} ({dimensione}MB)"

async def scarica_multipli_file():
    """Scarica multipli file contemporaneamente"""
    risultati = await asyncio.gather(
        scarica_file("file1.zip", 50),
        scarica_file("file2.pdf", 20),
        scarica_file("file3.mp4", 100)
    )
    return risultati

risultati = asyncio.run(scarica_multipli_file())
print(f"File scaricati: {risultati}")


# 5. Gestione errori in codice asincrono

print("\n--- Gestione Errori ---")

async def operazione_con_errore(nome, fallisce=False):
    """Operazione che può fallire"""
    print(f"Inizio {nome}")
    await asyncio.sleep(1)
    if fallisce:
        raise ValueError(f"Errore in {nome}")
    print(f"Fine {nome}")
    return f"Successo: {nome}"

async def gestisci_errori():
    """Gestisce errori in operazioni asincrone"""
    try:
        risultati = await asyncio.gather(
            operazione_con_errore("Op1", False),
            operazione_con_errore("Op2", True),  # Questa fallisce
            operazione_con_errore("Op3", False),
            return_exceptions=True  # Restituisce eccezioni invece di propagarle
        )
        
        for i, risultato in enumerate(risultati):
            if isinstance(risultato, Exception):
                print(f"Operazione {i+1} fallita: {risultato}")
            else:
                print(f"Operazione {i+1}: {risultato}")
                
    except Exception as e:
        print(f"Errore generale: {e}")

asyncio.run(gestisci_errori())


# 6. Timeout

print("\n--- Timeout ---")

async def operazione_lunga():
    """Operazione che richiede molto tempo"""
    print("Inizio operazione lunga...")
    await asyncio.sleep(10)
    print("Operazione completata")
    return "Risultato"

async def con_timeout():
    """Esegue un'operazione con timeout"""
    try:
        # Timeout di 2 secondi
        risultato = await asyncio.wait_for(operazione_lunga(), timeout=2.0)
        print(f"Risultato: {risultato}")
    except asyncio.TimeoutError:
        print("Operazione interrotta: timeout!")

asyncio.run(con_timeout())


# 7. asyncio.wait() - Controllo più granulare

print("\n--- asyncio.wait() ---")

async def task_con_durata(nome, durata):
    """Task con durata specifica"""
    await asyncio.sleep(durata)
    return f"{nome} completato"

async def usa_wait():
    """Usa asyncio.wait() per controllo avanzato"""
    tasks = [
        asyncio.create_task(task_con_durata("Task1", 1)),
        asyncio.create_task(task_con_durata("Task2", 2)),
        asyncio.create_task(task_con_durata("Task3", 3))
    ]
    
    # Aspetta che almeno un task completi
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    
    print(f"Task completati: {len(done)}")
    print(f"Task in attesa: {len(pending)}")
    
    # Cancella i task rimanenti
    for task in pending:
        task.cancel()

asyncio.run(usa_wait())


# 8. Generatori asincroni

print("\n--- Generatori Asincroni ---")

async def generatore_numeri(n):
    """Generatore asincrono che produce numeri"""
    for i in range(n):
        await asyncio.sleep(0.5)
        yield i

async def usa_generatore():
    """Usa un generatore asincrono"""
    async for numero in generatore_numeri(5):
        print(f"Numero ricevuto: {numero}")

asyncio.run(usa_generatore())


# 9. Context Manager asincroni

print("\n--- Context Manager Asincroni ---")

class ConnessioneDatabase:
    """Simula una connessione database asincrona"""
    
    async def __aenter__(self):
        print("Connessione al database...")
        await asyncio.sleep(1)
        print("Connesso!")
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Chiusura connessione...")
        await asyncio.sleep(0.5)
        print("Connessione chiusa")
        return False
    
    async def query(self, sql):
        print(f"Esecuzione query: {sql}")
        await asyncio.sleep(0.5)
        return ["risultato1", "risultato2"]

async def usa_database():
    """Usa un context manager asincrono"""
    async with ConnessioneDatabase() as db:
        risultati = await db.query("SELECT * FROM users")
        print(f"Risultati: {risultati}")

asyncio.run(usa_database())


# 10. Semafori per limitare concorrenza

print("\n--- Semafori ---")

async def richiesta_api(nome, semaforo):
    """Simula una richiesta API con limite di concorrenza"""
    async with semaforo:  # Acquisisce il semaforo
        print(f"Inizio richiesta: {nome}")
        await asyncio.sleep(2)
        print(f"Fine richiesta: {nome}")
        return f"Dati da {nome}"

async def limita_concorrenza():
    """Limita il numero di richieste simultanee"""
    # Permette massimo 2 richieste contemporanee
    semaforo = asyncio.Semaphore(2)
    
    tasks = [
        richiesta_api(f"API-{i}", semaforo)
        for i in range(5)
    ]
    
    risultati = await asyncio.gather(*tasks)
    return risultati

risultati = asyncio.run(limita_concorrenza())
print(f"Risultati: {risultati}")


# 11. Lock per sincronizzazione

print("\n--- Lock ---")

class Contatore:
    """Contatore thread-safe con lock asincrono"""
    
    def __init__(self):
        self.valore = 0
        self.lock = asyncio.Lock()
    
    async def incrementa(self, nome):
        async with self.lock:
            print(f"{nome}: lettura valore {self.valore}")
            await asyncio.sleep(0.1)  # Simula operazione
            self.valore += 1
            print(f"{nome}: valore incrementato a {self.valore}")

async def usa_lock():
    """Usa lock per sincronizzare accesso a risorsa condivisa"""
    contatore = Contatore()
    
    await asyncio.gather(
        contatore.incrementa("Task1"),
        contatore.incrementa("Task2"),
        contatore.incrementa("Task3")
    )
    
    print(f"Valore finale: {contatore.valore}")

asyncio.run(usa_lock())


# 12. Queue asincrona

print("\n--- Queue Asincrona ---")

async def produttore(queue, nome):
    """Produce elementi e li mette nella queue"""
    for i in range(3):
        elemento = f"{nome}-{i}"
        await queue.put(elemento)
        print(f"Prodotto: {elemento}")
        await asyncio.sleep(1)

async def consumatore(queue, nome):
    """Consuma elementi dalla queue"""
    while True:
        elemento = await queue.get()
        print(f"{nome} ha consumato: {elemento}")
        await asyncio.sleep(0.5)
        queue.task_done()

async def usa_queue():
    """Usa queue per comunicazione producer-consumer"""
    queue = asyncio.Queue()
    
    # Creare produttori e consumatori
    produttori = [
        asyncio.create_task(produttore(queue, f"Prod{i}"))
        for i in range(2)
    ]
    
    consumatori = [
        asyncio.create_task(consumatore(queue, f"Cons{i}"))
        for i in range(2)
    ]
    
    # Aspettare che i produttori finiscano
    await asyncio.gather(*produttori)
    
    # Aspettare che la queue sia vuota
    await queue.join()
    
    # Cancellare i consumatori
    for c in consumatori:
        c.cancel()

asyncio.run(usa_queue())


# 13. Esempio pratico: Web scraper asincrono

print("\n--- Web Scraper Asincrono (simulato) ---")

async def scarica_pagina(url):
    """Simula il download di una pagina web"""
    print(f"Download: {url}")
    await asyncio.sleep(1)  # Simula richiesta HTTP
    return f"Contenuto di {url}"

async def processa_pagina(contenuto):
    """Processa il contenuto della pagina"""
    await asyncio.sleep(0.5)  # Simula processing
    return f"Processato: {contenuto}"

async def scraper(urls):
    """Scraper asincrono per multiple URL"""
    # Download di tutte le pagine contemporaneamente
    contenuti = await asyncio.gather(*[scarica_pagina(url) for url in urls])
    
    # Processing di tutti i contenuti contemporaneamente
    risultati = await asyncio.gather(*[processa_pagina(c) for c in contenuti])
    
    return risultati

urls = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3"
]

risultati = asyncio.run(scraper(urls))
for risultato in risultati:
    print(risultato)


# 14. Best practices

print("\n--- Best Practices ---")
print("""
✅ Usa async/await per operazioni I/O (rete, file, database)
✅ Usa asyncio.gather() per eseguire multipli task in parallelo
✅ Gestisci timeout con asyncio.wait_for()
✅ Usa semafori per limitare la concorrenza
✅ Gestisci errori con try/except e return_exceptions=True

❌ Non usare async per operazioni CPU-intensive (usa multiprocessing)
❌ Non bloccare l'event loop con time.sleep() (usa asyncio.sleep())
❌ Non dimenticare await davanti a coroutine
❌ Non mescolare codice sincrono bloccante con async
""")


# 15. Quando usare la programmazione asincrona

print("\n--- Quando Usare Async ---")
print("""
✅ USALA per:
- Richieste HTTP multiple
- Operazioni database concorrenti
- Lettura/scrittura file multipli
- WebSocket e real-time communication
- Operazioni I/O che richiedono attesa

❌ NON usarla per:
- Calcoli matematici intensivi
- Elaborazione immagini/video
- Operazioni CPU-bound
- Codice semplice senza I/O
(Per CPU-bound usa multiprocessing o threading)
""")
