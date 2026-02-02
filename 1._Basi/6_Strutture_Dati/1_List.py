# Le liste sono uno dei tipi di dati più versatili in Python.
# Una lista è una raccolta ordinata e modificabile di elementi.
# Le liste possono contenere elementi di tipi diversi.

# 1. Creazione di una lista
# Una lista si crea utilizzando le parentesi quadre [].
lista_vuota = []
print(f"Lista vuota: {lista_vuota}")

lista_numeri = [1, 5, 2, 8, 3]
print(f"Lista di numeri: {lista_numeri}")

lista_stringhe = ["ciao", "mondo", "python"]
print(f"Lista di stringhe: {lista_stringhe}")

lista_mista = [10, "test", True, 3.14]
print(f"Lista con tipi di dati misti: {lista_mista}")


# 2. Accesso agli elementi
# Gli elementi di una lista si accedono tramite un indice, che parte da 0.
primo_elemento = lista_numeri[0]  # Accede al primo elemento (1)
print(f"Il primo elemento della lista_numeri è: {primo_elemento}")

secondo_elemento = lista_stringhe[1] # Accede al secondo elemento ("mondo")
print(f"Il secondo elemento della lista_stringhe è: {secondo_elemento}")

# L'indicizzazione negativa parte dalla fine della lista.
ultimo_elemento = lista_numeri[-1] # Accede all'ultimo elemento (3)
print(f"L'ultimo elemento della lista_numeri è: {ultimo_elemento}")


# 3. Modifica degli elementi
# Le liste sono modificabili (mutabili).
print(f"Lista di stringhe prima della modifica: {lista_stringhe}")
lista_stringhe[1] = "a tutti" # Sostituisce "mondo" con "a tutti"
print(f"Lista di stringhe dopo la modifica: {lista_stringhe}")


# 4. Aggiunta di elementi
# .append() aggiunge un elemento alla fine della lista.
lista_numeri.append(100)
print(f"Lista numeri dopo .append(100): {lista_numeri}")

# .insert() inserisce un elemento in una posizione specifica.
lista_numeri.insert(2, 99) # Inserisce 99 all'indice 2
print(f"Lista numeri dopo .insert(2, 99): {lista_numeri}")


# 5. Rimozione di elementi
# .remove() rimuove la prima occorrenza di un valore specificato.
lista_stringhe.remove("python")
print(f"Lista stringhe dopo .remove('python'): {lista_stringhe}")

# .pop() rimuove e restituisce l'elemento a un dato indice (o l'ultimo se l'indice non è specificato).
elemento_rimosso = lista_numeri.pop(1) # Rimuove l'elemento all'indice 1 (5)
print(f"Elemento rimosso con .pop(1): {elemento_rimosso}")
print(f"Lista numeri dopo la rimozione: {lista_numeri}")


# 6. Metodi utili per le liste
# len() restituisce la lunghezza della lista.
lunghezza = len(lista_numeri)
print(f"La lunghezza di lista_numeri è: {lunghezza}")

# .sort() ordina la lista in loco (modifica la lista originale).
lista_disordinata = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Lista disordinata: {lista_disordinata}")
lista_disordinata.sort() # Ordina in modo crescente
print(f"Lista dopo .sort(): {lista_disordinata}")
lista_disordinata.sort(reverse=True) # Ordina in modo decrescente
print(f"Lista dopo .sort(reverse=True): {lista_disordinata}")

# sorted() restituisce una nuova lista ordinata senza modificare l'originale.
lista_originale = [3, 1, 4]
lista_ordinata_nuova = sorted(lista_originale)
print(f"Lista originale non modificata: {lista_originale}")
print(f"Nuova lista ordinata creata con sorted(): {lista_ordinata_nuova}")


# 7. Slicing (affettare) una lista
# Lo slicing permette di ottenere una sotto-lista.
# la sintassi è lista[inizio:fine:passo]
sotto_lista = lista_numeri[1:4] # Estrae gli elementi dall'indice 1 all'indice 3 (4 escluso)
print(f"Slicing di lista_numeri [1:4]: {sotto_lista}")

fino_alla_fine = lista_numeri[2:] # Dall'indice 2 fino alla fine
print(f"Slicing di lista_numeri [2:]: {fino_alla_fine}")

dall_inizio = lista_numeri[:3] # Dall'inizio fino all'indice 2 (3 escluso)
print(f"Slicing di lista_numeri [:3]: {dall_inizio}")
