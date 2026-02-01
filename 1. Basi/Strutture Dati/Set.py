# I set (insiemi) sono raccolte non ordinate e non indicizzate di elementi UNICI.
# Sono molto utili per operazioni matematiche sugli insiemi come unioni, intersezioni, differenze.
# e per rimuovere duplicati da una lista.

# 1. Creazione di un set
# Un set si crea usando le parentesi graffe {} o la funzione set().
# NOTA: per creare un set vuoto, si deve usare set(), perché {} crea un dizionario vuoto.
set_vuoto = set()
print(f"Set vuoto: {set_vuoto}")

numeri = {1, 2, 3, 4, 5, 5, 4} # I duplicati vengono rimossi automaticamente
print(f"Set di numeri (i duplicati sono rimossi): {numeri}")

# Creare un set da una lista (rimuove i duplicati)
lista_con_duplicati = [1, 2, 'a', 'b', 2, 'c', 'a']
set_da_lista = set(lista_con_duplicati)
print(f"Lista originale: {lista_con_duplicati}")
print(f"Set creato dalla lista: {set_da_lista}")


# 2. Accesso agli elementi
# I set sono non ordinati, quindi non si può accedere agli elementi tramite indice.
# Il seguente codice provocherà un errore (TypeError).
# print(numeri[0]) # -> TypeError: 'set' object is not subscriptable

# Per accedere agli elementi, di solito si itera sul set.
print("\nElementi nel set 'numeri':")
for elemento in numeri:
    print(elemento)


# 3. Aggiunta di elementi
# .add() aggiunge un singolo elemento.
numeri.add(6)
print(f"\nSet dopo .add(6): {numeri}")
numeri.add(1) # Aggiungere un elemento già presente non ha effetto
print(f"Set dopo .add(1) di nuovo: {numeri}")

# .update() aggiunge elementi da un altro set, lista, tupla, etc.
numeri.update({7, 8, 9})
print(f"Set dopo .update({{7, 8, 9}}): {numeri}")


# 4. Rimozione di elementi
# .remove() rimuove un elemento. Se l'elemento non è presente, solleva un errore (KeyError).
numeri.remove(9)
print(f"\nSet dopo .remove(9): {numeri}")
# numeri.remove(99) # -> KeyError: 99

# .discard() rimuove un elemento. Se l'elemento non è presente, NON solleva alcun errore.
numeri.discard(8)
print(f"Set dopo .discard(8): {numeri}")
numeri.discard(99) # Non fa nulla e non dà errore.
print(f"Set dopo .discard(99): {numeri}")


# 5. Operazioni tra insiemi (sets)
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(f"\nSet A: {set_a}")
print(f"Set B: {set_b}")

# Unione: elementi presenti in A, in B, o in entrambi.
unione = set_a.union(set_b) # oppure set_a | set_b
print(f"Unione (A | B): {unione}")

# Intersezione: elementi presenti sia in A che in B.
intersezione = set_a.intersection(set_b) # oppure set_a & set_b
print(f"Intersezione (A & B): {intersezione}")

# Differenza: elementi presenti in A ma non in B.
differenza = set_a.difference(set_b) # oppure set_a - set_b
print(f"Differenza (A - B): {differenza}")

# Differenza simmetrica: elementi presenti in A o in B, ma non in entrambi.
diff_simmetrica = set_a.symmetric_difference(set_b) # oppure set_a ^ set_b
print(f"Differenza simmetrica (A ^ B): {diff_simmetrica}")
