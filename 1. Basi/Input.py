#Gli input ci permettono di ricevere dati dall'utente durante l'esecuzione del programma.
#sono molto utili per un interfaccia con gli utenti 

#Es -> String
nome=input("Inserisci il tuo nome: ")
anni=input("Inserisci la tua età: ")

print(f"E' un piacere {nome} di {anni}")

x=int(input("\nInserisci un numero intero: "))
y=int(input("Inserisci un altro numero intero: "))
somma=x+y
print(f"La somma di {x} e {y} è {somma}")

f=float(input("\nInserisci un numero decimale: "))
g=float(input("Inserisci un altro numero decimale: "))
somma_decimale=f+g
print(f"La somma di {f} e {g} è {somma_decimale}")

s=str(input("\nInserisci un numero intero da convertire in stringa: "))
print(f"Hai inserito il numero {s} che è di tipo {type(s)}")