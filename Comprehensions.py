# Le comprehensions sono un modo elegante e conciso per creare liste, dizionari e set in Python.
# Sono più veloci e leggibili rispetto ai loop tradizionali quando usate correttamente.
# Seguono il paradigma della programmazione funzionale.

# 1. LIST COMPREHENSIONS
# Sintassi base: [espressione for elemento in iterabile]

# Esempio tradizionale con for loop
numeri = []
for i in range(10):
    numeri.append(i)
print(f"Con for loop: {numeri}")

# Stesso risultato con list comprehension
numeri_comp = [i for i in range(10)]
print(f"Con list comprehension: {numeri_comp}")


# 2. List comprehension con condizione
# Sintassi: [espressione for elemento in iterabile if condizione]

# Creare una lista di numeri pari
pari_tradizionale = []
for i in range(20):
    if i % 2 == 0:
        pari_tradizionale.append(i)
print(f"\nNumeri pari (tradizionale): {pari_tradizionale}")

# Con list comprehension
pari = [i for i in range(20) if i % 2 == 0]
print(f"Numeri pari (comprehension): {pari}")


# 3. List comprehension con trasformazione

# Quadrati dei numeri
quadrati = [x**2 for x in range(10)]
print(f"\nQuadrati: {quadrati}")

# Convertire stringhe in maiuscolo
parole = ["ciao", "mondo", "python"]
maiuscole = [parola.upper() for parola in parole]
print(f"Parole in maiuscolo: {maiuscole}")

# Estrarre lunghezze delle stringhe
lunghezze = [len(parola) for parola in parole]
print(f"Lunghezze delle parole: {lunghezze}")


# 4. List comprehension con if-else
# Sintassi: [espressione_se_vero if condizione else espressione_se_falso for elemento in iterabile]

# Classificare numeri come pari o dispari
classificazione = ["pari" if x % 2 == 0 else "dispari" for x in range(10)]
print(f"\nClassificazione: {classificazione}")

# Sostituire valori negativi con 0
numeri_misti = [5, -3, 8, -1, 0, 12, -7]
positivi = [x if x >= 0 else 0 for x in numeri_misti]
print(f"Numeri negativi sostituiti con 0: {positivi}")


# 5. List comprehension annidate
# Creare una matrice (lista di liste)
matrice = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(f"\nMatrice 3x3:")
for riga in matrice:
    print(riga)

# Appiattire una matrice (flatten)
matrice_esempio = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
appiattita = [elemento for riga in matrice_esempio for elemento in riga]
print(f"Matrice appiattita: {appiattita}")


# 6. DICTIONARY COMPREHENSIONS
# Sintassi: {chiave: valore for elemento in iterabile}

# Creare un dizionario di quadrati
quadrati_dict = {x: x**2 for x in range(6)}
print(f"\nDizionario di quadrati: {quadrati_dict}")

# Invertire un dizionario (scambiare chiavi e valori)
originale = {"a": 1, "b": 2, "c": 3}
invertito = {valore: chiave for chiave, valore in originale.items()}
print(f"Dizionario originale: {originale}")
print(f"Dizionario invertito: {invertito}")

# Dictionary comprehension con condizione
# Solo numeri pari
pari_dict = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"Dizionario con solo numeri pari: {pari_dict}")


# 7. Dictionary comprehension da due liste
nomi = ["Alice", "Bob", "Charlie"]
eta = [25, 30, 35]

# Creare un dizionario combinando due liste
persone = {nome: anni for nome, anni in zip(nomi, eta)}
print(f"\nDizionario persone: {persone}")


# 8. Dictionary comprehension con trasformazione
# Convertire chiavi in maiuscolo
frutta = {"mela": 3, "banana": 5, "arancia": 2}
frutta_maiuscola = {chiave.upper(): valore for chiave, valore in frutta.items()}
print(f"Frutta con chiavi maiuscole: {frutta_maiuscola}")

# Filtrare un dizionario
# Solo frutti con quantità > 2
frutta_filtrata = {chiave: valore for chiave, valore in frutta.items() if valore > 2}
print(f"Frutta con quantità > 2: {frutta_filtrata}")


# 9. SET COMPREHENSIONS
# Sintassi: {espressione for elemento in iterabile}
# I set non contengono duplicati e non sono ordinati

# Creare un set di quadrati
quadrati_set = {x**2 for x in range(10)}
print(f"\nSet di quadrati: {quadrati_set}")

# Set comprehension con condizione
# Solo numeri dispari
dispari_set = {x for x in range(20) if x % 2 != 0}
print(f"Set di numeri dispari: {dispari_set}")

# Rimuovere duplicati da una lista usando set comprehension
lista_con_duplicati = [1, 2, 2, 3, 4, 4, 5, 5, 5]
senza_duplicati = {x for x in lista_con_duplicati}
print(f"Lista con duplicati: {lista_con_duplicati}")
print(f"Set senza duplicati: {senza_duplicati}")


# 10. GENERATOR EXPRESSIONS
# Simili alle list comprehensions ma usano parentesi tonde ()
# Generano valori uno alla volta (lazy evaluation) invece di creare l'intera lista in memoria
# Più efficienti per grandi dataset

# List comprehension (crea tutta la lista in memoria)
lista_grande = [x**2 for x in range(1000000)]
print(f"\nList comprehension creata (usa molta memoria)")

# Generator expression (genera valori uno alla volta)
generatore = (x**2 for x in range(1000000))
print(f"Generator expression creato: {generatore}")
print(f"Primo valore del generatore: {next(generatore)}")
print(f"Secondo valore del generatore: {next(generatore)}")


# 11. Esempi pratici

# Esempio 1: Filtrare e trasformare dati
studenti = [
    {"nome": "Alice", "voto": 85},
    {"nome": "Bob", "voto": 92},
    {"nome": "Charlie", "voto": 78},
    {"nome": "Diana", "voto": 95}
]

# Ottenere nomi degli studenti con voto >= 90
studenti_eccellenti = [s["nome"] for s in studenti if s["voto"] >= 90]
print(f"\nStudenti con voto >= 90: {studenti_eccellenti}")

# Esempio 2: Processare stringhe
frase = "Python è un linguaggio fantastico"
# Contare lunghezza di ogni parola
lunghezze_parole = {parola: len(parola) for parola in frase.split()}
print(f"Lunghezza delle parole: {lunghezze_parole}")

# Esempio 3: Operazioni matematiche
# Creare una tabella pitagorica
tabella_pitagorica = {f"{i}x{j}": i*j for i in range(1, 6) for j in range(1, 6)}
print(f"\nTabella pitagorica (primi 5 numeri):")
for chiave, valore in list(tabella_pitagorica.items())[:10]:
    print(f"{chiave} = {valore}")


# 12. Quando usare le comprehensions

# ✅ USALE quando:
# - La logica è semplice e leggibile
# - Vuoi creare una nuova collezione da una esistente
# - Hai bisogno di filtrare e trasformare dati

# ❌ NON usarle quando:
# - La logica è troppo complessa (meglio un loop tradizionale)
# - Hai bisogno di gestire eccezioni
# - Devi eseguire operazioni con effetti collaterali

# Esempio di comprehension troppo complessa (da evitare)
# risultato = [x**2 if x > 0 else abs(x) if x < 0 else 0 for x in range(-5, 5) if x != 0]

# Meglio usare un loop tradizionale per logica complessa
risultato = []
for x in range(-5, 5):
    if x != 0:
        if x > 0:
            risultato.append(x**2)
        else:
            risultato.append(abs(x))
    else:
        risultato.append(0)
print(f"\nLogica complessa (meglio con loop): {risultato}")
