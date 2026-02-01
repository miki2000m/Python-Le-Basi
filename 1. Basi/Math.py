#L'informatica è principalmente basata su operazioni matematiche.
#Questo modulo contiene alcune funzioni matematiche di base.

#Es -> Somma
a=5
b=3
somma=a+b
print(f"La somma di {a} e {b} è {somma}")
#Es -> Sottrazione
sottrazione=a-b
print(f"La sottrazione di {a} e {b} è {sottrazione}")
#Es -> Moltiplicazione
moltiplicazione=a*b
print(f"La moltiplicazione di {a} e {b} è {moltiplicazione}")
#Es -> Divisione
divisione=a/b
print(f"La divisione di {a} e {b} è {divisione}")

#Es -> Massimo e minimo
#Questo metodo è molto utile per confontare due numeri al posto di usare un if statement
massimo=max(a, b)
minimo=min(a, b)
print(f"Il massimo tra {a} e {b} è {massimo}")
print(f"Il minimo tra {a} e {b} è {minimo}")

#Oltre a queste operazioni di base, 
#Python offre un modulo matematico più avanzato chiamato 'math' che include funzioni come radice quadrata, potenza, logaritmi, e funzioni trigonometriche.
import math 

#Es -> Valore assoluto
valore_assoluto=math.fabs(-10)
print(f"Il valore assoluto di -10 è {valore_assoluto}")
#Es -> Radice quadrata
radice_quadrata=math.sqrt(16)
print(f"La radice quadrata di 16 è {radice_quadrata}")
#Es -> Potenza
potenza=math.pow(2, 3)
print(f"2 elevato alla 3 è {potenza}")
#Es -> Logaritmo
logaritmo=math.log(100, 10)
print(f"Il logaritmo in base 10 di 100 è {logaritmo}")
#Es -> Seno
seno=math.sin(math.pi/2)
print(f"Il seno di 90 gradi (π/2 radianti) è {seno}")

#Poi ci sono le funzioni di arrotondamento
#Es -> Arrotondamento per difetto
arrotondamento_per_difetto=math.floor(4.7)
print(f"Arrotondamento per difetto di 4.7 è {arrotondamento_per_difetto}")
#Es -> Arrotondamento per eccesso
arrotondamento_per_eccesso=math.ceil(4.3)
print(f"Arrotondamento per eccesso di 4.3 è {arrotondamento_per_eccesso}")
#Es -> Arrotondamento normale
arrotondamento_normale=round(4.5)
print(f"Arrotondamento normale di 4.5 è {arrotondamento_normale}")

#Poi ci sono le costanti matematiche
#Es -> Pi greco
pi_greco=math.pi
print(f"Il valore di Pi greco è {pi_greco}")
#Es -> Numero di Eulero
numero_eulero=math.e
print(f"Il valore del numero di Eulero è {numero_eulero}")

#In fine per aggevolare l'uso delle funzioni matematiche
#possiamo importare tutte le funzioni del modulo math direttamente nel nostro spazio dei nomi
from math import *

#Es -> Uso diretto della funzione radice quadrata
radice_quadrata_diretta=sqrt(25)
print(f"La radice quadrata di 25 è {radice_quadrata_diretta}")
#Es -> Uso diretto della funzione potenza
potenza_diretta=pow(3, 4)
print(f"3 elevato alla 4 è {potenza_diretta}")
#Es -> Uso diretto della funzione seno
seno_diretto=sin(pi/6)
print(f"Il seno di 30 gradi (π/6 radianti) è {seno_diretto}")
#Es -> Uso diretto della costante Pi greco
print(f"Il valore di Pi greco è {pi}")
#Es -> Uso diretto della costante Numero di Eulero
print(f"Il valore del numero di Eulero è {e}")

