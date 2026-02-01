# Questo file 'main.py' userà il codice definito in 'mymodule.py'.
# Per usare le funzioni, classi o variabili di un altro file (modulo), dobbiamo importarlo.

# 1. Importare l'intero modulo
# In questo caso, per accedere agli elementi del modulo, dobbiamo usare il prefisso 'mymodule.'.
import mymodule

print("--- Usando 'import mymodule' ---")
saluto = mymodule.saluta("Alice")
print(saluto)

pi = mymodule.PI_GRECO
print(f"Il valore di PI_GRECO importato è: {pi}")

calcolatrice1 = mymodule.CalcolatriceSemplice()
print(f"Calcolo da mymodule: 10 * 5 = {calcolatrice1.moltiplica(10, 5)}")


# 2. Importare elementi specifici da un modulo
# Con la parola chiave 'from', possiamo importare solo ciò che ci serve.
# Questo ci permette di usare i nomi direttamente, senza il prefisso del modulo.
from mymodule import saluta, PI_GRECO

print("\n--- Usando 'from mymodule import ...' ---")
saluto_diretto = saluta("Bob") # Non serve 'mymodule.'
print(saluto_diretto)
print(f"Il valore di PI_GRECO importato direttamente è: {PI_GRECO}")


# 3. Importare e rinominare (usando 'as')
# 'as' può essere usato per dare un alias (un soprannome) a un modulo o a un elemento importato.
# È utile per evitare conflitti di nomi o per abbreviare nomi lunghi.

import mymodule as mm
from mymodule import CalcolatriceSemplice as Calcolatrice

print("\n--- Usando 'as' per rinominare ---")
print(mm.saluta("Carlo")) # Usiamo l'alias 'mm'

calcolatrice2 = Calcolatrice() # Usiamo l'alias 'Calcolatrice'
print(f"Calcolo con la classe rinominata: 7 + 8 = {calcolatrice2.somma(7, 8)}")


# I 'pacchetti' (packages) sono un modo per strutturare i moduli di Python.
# Un pacchetto è semplicemente una directory che contiene un file speciale __init__.py e altri moduli.
# Questo permette di avere una gerarchia di moduli, ad es. 'mio_pacchetto.sottopacchetto.modulo'.
# La struttura di questo progetto 'Python Le Basi' con le sue sottodirectory è simile al concetto di pacchetti.
