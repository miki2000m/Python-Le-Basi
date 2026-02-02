# Le funzioni lambda sono funzioni anonime (senza nome) che possono essere definite in una sola riga.
# Sono utili per operazioni semplici e quando si passano funzioni come argomenti.
# Sintassi: lambda parametri: espressione

# 1. Confronto tra funzione normale e lambda

# Funzione normale
def somma_normale(a, b):
    return a + b

# Funzione lambda equivalente
somma_lambda = lambda a, b: a + b

print("Confronto funzione normale vs lambda:")
print(f"Somma normale: {somma_normale(5, 3)}")
print(f"Somma lambda: {somma_lambda(5, 3)}")


# 2. Lambda con un solo parametro

# Funzione che raddoppia un numero
raddoppia = lambda x: x * 2
print(f"\nRaddoppia 10: {raddoppia(10)}")

# Funzione che calcola il quadrato
quadrato = lambda x: x ** 2
print(f"Quadrato di 7: {quadrato(7)}")


# 3. Lambda senza parametri

# Lambda che restituisce sempre lo stesso valore
saluto = lambda: "Ciao, mondo!"
print(f"\n{saluto()}")


# 4. Lambda con condizioni (if-else)

# Verifica se un numero è pari
e_pari = lambda x: "pari" if x % 2 == 0 else "dispari"
print(f"\n5 è {e_pari(5)}")
print(f"8 è {e_pari(8)}")

# Trova il massimo tra due numeri
massimo = lambda a, b: a if a > b else b
print(f"Massimo tra 15 e 23: {massimo(15, 23)}")


# 5. FUNZIONI DI ORDINE SUPERIORE
# Sono funzioni che accettano altre funzioni come parametri o le restituiscono come risultato

# 5.1 MAP()
# Applica una funzione a ogni elemento di un iterabile
# Sintassi: map(funzione, iterabile)

numeri = [1, 2, 3, 4, 5]

# Raddoppiare ogni numero
raddoppiati = list(map(lambda x: x * 2, numeri))
print(f"\nNumeri originali: {numeri}")
print(f"Numeri raddoppiati con map(): {raddoppiati}")

# Convertire temperature da Celsius a Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(f"\nCelsius: {celsius}")
print(f"Fahrenheit: {fahrenheit}")

# Map con più iterabili
numeri1 = [1, 2, 3, 4]
numeri2 = [10, 20, 30, 40]
somme = list(map(lambda x, y: x + y, numeri1, numeri2))
print(f"\nSomma di {numeri1} e {numeri2}: {somme}")


# 5.2 FILTER()
# Filtra elementi di un iterabile in base a una condizione
# Sintassi: filter(funzione, iterabile)

numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrare solo i numeri pari
pari = list(filter(lambda x: x % 2 == 0, numeri))
print(f"\nNumeri: {numeri}")
print(f"Solo pari con filter(): {pari}")

# Filtrare stringhe più lunghe di 5 caratteri
parole = ["ciao", "mondo", "python", "programmazione", "ai"]
lunghe = list(filter(lambda p: len(p) > 5, parole))
print(f"\nParole: {parole}")
print(f"Parole con più di 5 caratteri: {lunghe}")

# Filtrare numeri positivi
numeri_misti = [-5, 3, -1, 8, 0, -3, 12]
positivi = list(filter(lambda x: x > 0, numeri_misti))
print(f"\nNumeri misti: {numeri_misti}")
print(f"Solo positivi: {positivi}")


# 5.3 REDUCE()
# Applica una funzione cumulativamente agli elementi di un iterabile, riducendoli a un singolo valore
# Sintassi: reduce(funzione, iterabile)
# NOTA: reduce() si trova nel modulo functools

from functools import reduce

numeri = [1, 2, 3, 4, 5]

# Sommare tutti i numeri
somma_totale = reduce(lambda x, y: x + y, numeri)
print(f"\nNumeri: {numeri}")
print(f"Somma totale con reduce(): {somma_totale}")

# Moltiplicare tutti i numeri (fattoriale)
prodotto = reduce(lambda x, y: x * y, numeri)
print(f"Prodotto di tutti i numeri: {prodotto}")

# Trovare il massimo
numeri_casuali = [45, 23, 78, 12, 89, 34]
massimo = reduce(lambda x, y: x if x > y else y, numeri_casuali)
print(f"\nNumeri: {numeri_casuali}")
print(f"Massimo con reduce(): {massimo}")


# 6. SORTED() con lambda
# Ordinare strutture dati complesse usando lambda come chiave

# Ordinare una lista di tuple per il secondo elemento
coppie = [(1, 'uno'), (3, 'tre'), (2, 'due'), (4, 'quattro')]
ordinate = sorted(coppie, key=lambda x: x[1])
print(f"\nCoppie originali: {coppie}")
print(f"Ordinate per secondo elemento: {ordinate}")

# Ordinare dizionari per valore
studenti = [
    {"nome": "Alice", "voto": 85},
    {"nome": "Bob", "voto": 92},
    {"nome": "Charlie", "voto": 78},
    {"nome": "Diana", "voto": 95}
]

# Ordinare per voto (crescente)
per_voto = sorted(studenti, key=lambda s: s["voto"])
print(f"\nStudenti ordinati per voto:")
for s in per_voto:
    print(f"  {s['nome']}: {s['voto']}")

# Ordinare per voto (decrescente)
per_voto_desc = sorted(studenti, key=lambda s: s["voto"], reverse=True)
print(f"\nStudenti ordinati per voto (decrescente):")
for s in per_voto_desc:
    print(f"  {s['nome']}: {s['voto']}")

# Ordinare stringhe per lunghezza
parole = ["python", "è", "fantastico", "e", "potente"]
per_lunghezza = sorted(parole, key=lambda p: len(p))
print(f"\nParole ordinate per lunghezza: {per_lunghezza}")


# 7. Combinare map(), filter() e reduce()

# Esempio: Calcolare la somma dei quadrati dei numeri pari
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Passo 1: Filtrare i numeri pari
pari = filter(lambda x: x % 2 == 0, numeri)

# Passo 2: Calcolare i quadrati
quadrati = map(lambda x: x ** 2, pari)

# Passo 3: Sommare tutti i quadrati
somma_quadrati = reduce(lambda x, y: x + y, quadrati)

print(f"\nNumeri: {numeri}")
print(f"Somma dei quadrati dei numeri pari: {somma_quadrati}")

# Stesso risultato in una sola riga
risultato = reduce(lambda x, y: x + y, map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numeri)))
print(f"Risultato in una riga: {risultato}")


# 8. Lambda in list comprehensions (alternativa)

# Invece di usare map() e filter(), spesso è più leggibile usare list comprehensions
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Con map() e filter()
risultato_lambda = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numeri)))

# Con list comprehension (più leggibile)
risultato_comp = [x ** 2 for x in numeri if x % 2 == 0]

print(f"\nCon map() e filter(): {risultato_lambda}")
print(f"Con list comprehension: {risultato_comp}")


# 9. Lambda con metodi di liste

# Usare lambda con min() e max()
persone = [
    {"nome": "Alice", "eta": 25},
    {"nome": "Bob", "eta": 30},
    {"nome": "Charlie", "eta": 22}
]

piu_giovane = min(persone, key=lambda p: p["eta"])
piu_vecchio = max(persone, key=lambda p: p["eta"])

print(f"\nPersona più giovane: {piu_giovane['nome']} ({piu_giovane['eta']} anni)")
print(f"Persona più vecchia: {piu_vecchio['nome']} ({piu_vecchio['eta']} anni)")


# 10. Limitazioni delle lambda

# Le lambda sono limitate a una sola espressione
# NON possono contenere:
# - Statements (come print, return, raise)
# - Assegnamenti
# - Annotazioni
# - Più di una espressione

# ❌ Questo NON funziona:
# lambda x: print(x)  # print è uno statement, non un'espressione

# ✅ Questo funziona (ma non è consigliato):
# lambda x: (print(x), x)[1]  # Trucco per eseguire print, ma è brutto

# Per logica complessa, usa una funzione normale
def funzione_complessa(x):
    if x < 0:
        print("Numero negativo")
        return 0
    elif x == 0:
        print("Zero")
        return 0
    else:
        print("Numero positivo")
        return x ** 2


# 11. Quando usare lambda

# ✅ USALE quando:
# - Hai bisogno di una funzione semplice e breve
# - La funzione viene usata una sola volta
# - Passi la funzione come argomento (map, filter, sorted, ecc.)

# ❌ NON usarle quando:
# - La logica è complessa
# - Hai bisogno di documentazione (docstring)
# - La funzione viene riutilizzata più volte (meglio una funzione normale con nome)


# 12. Esempio pratico completo

# Processare una lista di prodotti
prodotti = [
    {"nome": "Laptop", "prezzo": 1200, "categoria": "elettronica"},
    {"nome": "Mouse", "prezzo": 25, "categoria": "elettronica"},
    {"nome": "Libro", "prezzo": 15, "categoria": "libri"},
    {"nome": "Tastiera", "prezzo": 75, "categoria": "elettronica"},
    {"nome": "Penna", "prezzo": 2, "categoria": "cancelleria"}
]

print("\n--- Esempio pratico: Gestione prodotti ---")

# 1. Filtrare prodotti elettronici
elettronica = list(filter(lambda p: p["categoria"] == "elettronica", prodotti))
print(f"\nProdotti elettronici: {[p['nome'] for p in elettronica]}")

# 2. Applicare uno sconto del 10% ai prezzi
con_sconto = list(map(lambda p: {**p, "prezzo": p["prezzo"] * 0.9}, prodotti))
print(f"\nPrezzi con sconto 10%:")
for p in con_sconto:
    print(f"  {p['nome']}: €{p['prezzo']:.2f}")

# 3. Calcolare il prezzo totale
prezzo_totale = reduce(lambda acc, p: acc + p["prezzo"], prodotti, 0)
print(f"\nPrezzo totale: €{prezzo_totale:.2f}")

# 4. Trovare il prodotto più costoso
piu_costoso = max(prodotti, key=lambda p: p["prezzo"])
print(f"\nProdotto più costoso: {piu_costoso['nome']} (€{piu_costoso['prezzo']})")

# 5. Ordinare per prezzo
per_prezzo = sorted(prodotti, key=lambda p: p["prezzo"])
print(f"\nProdotti ordinati per prezzo:")
for p in per_prezzo:
    print(f"  {p['nome']}: €{p['prezzo']}")
