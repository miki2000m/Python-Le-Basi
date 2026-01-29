# I dizionari sono raccolte non ordinate, modificabili e indicizzate di coppie chiave-valore.
# Sono estremamente utili per memorizzare dati in modo strutturato.
# In altri linguaggi sono conosciuti come "hash map", "hash table" o "oggetti".

# 1. Creazione di un dizionario
# Un dizionario si crea usando le parentesi graffe {} con coppie chiave:valore.
dizionario_vuoto = {}
print(f"Dizionario vuoto: {dizionario_vuoto}")

persona = {
    "nome": "Mario",
    "cognome": "Rossi",
    "eta": 30,
    "citta": "Roma"
}
print(f"Dizionario 'persona': {persona}")


# 2. Accesso ai valori
# Si accede a un valore tramite la sua chiave.
nome_persona = persona["nome"]
print(f"Il nome della persona è: {nome_persona}")

# Se si tenta di accedere a una chiave che non esiste, si ottiene un errore (KeyError).
# print(persona["lavoro"]) # -> KeyError: 'lavoro'

# Per evitare errori, si può usare il metodo .get().
# .get() restituisce None (o un valore di default specificato) se la chiave non esiste.
lavoro_persona = persona.get("lavoro")
print(f"Il lavoro della persona è: {lavoro_persona}") # Stampa None

lavoro_persona_default = persona.get("lavoro", "Non specificato")
print(f"Il lavoro della persona (con default) è: {lavoro_persona_default}")


# 3. Modifica e aggiunta di elementi
# Si può modificare un valore esistente o aggiungere una nuova coppia chiave-valore.
print(f"Dizionario 'persona' prima della modifica: {persona}")
persona["eta"] = 31 # Modifica il valore associato alla chiave "eta"
persona["lavoro"] = "Ingegnere" # Aggiunge una nuova coppia chiave-valore
print(f"Dizionario 'persona' dopo la modifica: {persona}")

# Il metodo .update() può essere usato per aggiungere o modificare più coppie contemporaneamente.
persona.update({"citta": "Milano", "hobby": "Musica"})
print(f"Dizionario 'persona' dopo .update(): {persona}")


# 4. Rimozione di elementi
# .pop() rimuove una coppia chiave-valore e restituisce il valore.
hobby_rimosso = persona.pop("hobby")
print(f"Hobby rimosso: {hobby_rimosso}")
print(f"Dizionario dopo .pop('hobby'): {persona}")

# del rimuove una coppia chiave-valore.
del persona["citta"]
print(f"Dizionario dopo del persona['citta']: {persona}")


# 5. Iterare su un dizionario
# È possibile iterare su chiavi, valori o entrambi.

# Iterare sulle chiavi (comportamento di default)
print("\nIterazione sulle chiavi:")
for chiave in persona:
    print(f"Chiave: {chiave}, Valore: {persona[chiave]}")

# Ottenere le chiavi con il metodo .keys()
print(f"\nMetodo .keys(): {persona.keys()}")

# Ottenere i valori con il metodo .values()
print(f"Metodo .values(): {persona.values()}")
for valore in persona.values():
    print(f"Valore: {valore}")

# Iterare su coppie chiave-valore con il metodo .items()
print("\nIterazione su chiave e valore con .items():")
for chiave, valore in persona.items():
    print(f"Chiave: {chiave}, Valore: {valore}")


# 6. Altri metodi utili
# len() restituisce il numero di coppie chiave-valore.
print(f"\nIl dizionario 'persona' ha {len(persona)} elementi.")

# 'in' controlla se una chiave esiste nel dizionario.
if "nome" in persona:
    print("'nome' è una chiave del dizionario.")
if "indirizzo" not in persona:
    print("'indirizzo' non è una chiave del dizionario.")
