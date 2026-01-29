# Il ciclo 'for' in Python è usato per iterare su una sequenza (come una lista, una tupla, un dizionario, un set o una stringa).
# Permette di eseguire un blocco di codice per ogni elemento della sequenza.

# 1. Iterare su una lista
frutti = ["mela", "banana", "ciliegia"]
print("Iterazione su una lista di frutti:")
for frutto in frutti:
    print(frutto)


# 2. Iterare su una stringa
# Una stringa è una sequenza di caratteri, quindi possiamo iterare su di essa.
messaggio = "Ciao"
print("\nIterazione su una stringa:")
for carattere in messaggio:
    print(carattere)


# 3. La funzione range()
# Per eseguire un'azione un certo numero di volte, si usa la funzione range().
# range(5) genera numeri da 0 a 4.
print("\nUtilizzo di range(5):")
for i in range(5):
    print(f"Iterazione numero {i}")

# range() può anche avere un inizio e una fine: range(inizio, fine)
print("\nUtilizzo di range(2, 6):")
for i in range(2, 6): # Numeri da 2 a 5
    print(f"Numero: {i}")

# E anche un "passo": range(inizio, fine, passo)
print("\nUtilizzo di range(0, 10, 2):")
for i in range(0, 10, 2): # Numeri pari da 0 a 8
    print(f"Numero pari: {i}")


# 4. L'istruzione 'break'
# 'break' interrompe il ciclo immediatamente, anche se non sono stati processati tutti gli elementi.
print("\nUtilizzo di 'break':")
for frutto in frutti:
    if frutto == "banana":
        print("Trovata la banana! Interrompo il ciclo.")
        break
    print(frutto)


# 5. L'istruzione 'continue'
# 'continue' salta il resto del codice all'interno del ciclo per l'iterazione corrente e passa all'elemento successivo.
print("\nUtilizzo di 'continue':")
for frutto in frutti:
    if frutto == "banana":
        print("Salto la banana...")
        continue
    print(frutto)


# 6. Il blocco 'else' in un ciclo 'for'
# Il blocco 'else' viene eseguito quando il ciclo termina normalmente (cioè non viene interrotto da un 'break').
print("\nUtilizzo del blocco 'else':")
for i in range(3):
    print(f"Iterazione {i}")
else:
    print("Il ciclo è terminato senza interruzioni.")

print("\nUtilizzo del blocco 'else' con 'break':")
for i in range(3):
    print(f"Iterazione {i}")
    if i == 1:
        break
else:
    # Questo blocco non verrà eseguito perché il ciclo è stato interrotto.
    print("Questo messaggio non verrà stampato.")


# 7. Cicli annidati (Nested Loops)
# È possibile avere un ciclo all'interno di un altro ciclo.
print("\nEsempio di cicli annidati (tabelline):")
aggettivi = ["grande", "gustosa"]
frutti_per_aggettivi = ["mela", "banana"]

for aggettivo in aggettivi:
    for frutto in frutti_per_aggettivi:
        print(f"{aggettivo} {frutto}")


# 8. Iterare con 'enumerate'
# A volte è utile avere sia l'indice che l'elemento durante l'iterazione.
print("\nIterare con 'enumerate':")
for indice, frutto in enumerate(frutti):
    print(f"L'elemento all'indice {indice} è {frutto}")
