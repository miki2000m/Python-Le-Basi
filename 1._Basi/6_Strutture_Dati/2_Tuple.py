# Le tuple sono simili alle liste, ma con una differenza fondamentale: sono immutabili.
# Questo significa che una volta create, non possono essere modificate.
# Le tuple sono utili per rappresentare dati che non dovrebbero cambiare, come le coordinate.

# 1. Creazione di una tupla
# Una tupla si crea utilizzando le parentesi tonde ().
tupla_vuota = ()
print(f"Tupla vuota: {tupla_vuota}")

# Tupla con un solo elemento (notare la virgola finale, è importante per distinguerla da una semplice espressione tra parentesi)
tupla_singola = (1,)
print(f"Tupla con un solo elemento: {tupla_singola}")

tupla_numeri = (1, 5, 2, 8, 3)
print(f"Tupla di numeri: {tupla_numeri}")

tupla_mista = (10, "test", True, 3.14)
print(f"Tupla con tipi di dati misti: {tupla_mista}")

# Le parentesi sono opzionali in molti casi
altra_tupla = 1, 2, "hello"
print(f"Tupla creata senza parentesi: {altra_tupla}")


# 2. Accesso agli elementi
# L'accesso agli elementi è identico a quello delle liste, usando gli indici.
primo_elemento = tupla_numeri[0]
print(f"Il primo elemento della tupla_numeri è: {primo_elemento}")

ultimo_elemento = tupla_mista[-1]
print(f"L'ultimo elemento della tupla_mista è: {ultimo_elemento}")


# 3. Immutabilità
# A differenza delle liste, non è possibile modificare gli elementi di una tupla.
# Il seguente codice provocherà un errore (TypeError).
# tupla_numeri[0] = 100 # -> TypeError: 'tuple' object does not support item assignment
# print(tupla_numeri)

# Allo stesso modo, non si possono aggiungere o rimuovere elementi.
# tupla_numeri.append(10) # -> AttributeError: 'tuple' object has no attribute 'append'


# 4. Metodi delle tuple
# Le tuple hanno solo due metodi principali, poiché non possono essere modificate.
# .count() conta il numero di occorrenze di un valore.
occorrenze = tupla_numeri.count(5)
print(f"La tupla {tupla_numeri} contiene il numero 5 per {occorrenze} volte.")

# .index() restituisce l'indice della prima occorrenza di un valore.
indice = tupla_numeri.index(8)
print(f"L'indice del numero 8 nella tupla {tupla_numeri} è {indice}.")


# 5. "Unpacking" di una tupla
# È possibile assegnare i valori di una tupla a variabili separate.
coordinate = (10, 20, 30)
x, y, z = coordinate
print(f"Coordinate: x={x}, y={y}, z={z}")

# Questo è molto utile per le funzioni che restituiscono più valori (restituiscono una tupla).
def min_max(numeri):
    return (min(numeri), max(numeri))

minimo, massimo = min_max([1, 2, 3, 4, 5])
print(f"Il valore minimo è {minimo} e il massimo è {massimo}")


# 6. Perché usare le tuple?
# - Sicurezza: I dati non possono essere modificati accidentalmente.
# - Performance: Le tuple possono essere leggermente più veloci delle liste.
# - Chiavi di dizionario: Le tuple possono essere usate come chiavi in un dizionario (a differenza delle liste),
#   perché sono immutabili e quindi "hashable".
dizionario_con_tupla_chiave = {(0, 0): "Origine", (10, 20): "Punto A"}
print(f"Dizionario con chiavi di tipo tupla: {dizionario_con_tupla_chiave}")
