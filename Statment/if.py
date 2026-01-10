#Gli if sono delle strutture di controllo che ci permettono di eseguire del codice solo se una certa condizione è vera.
#La sintassi di base di un if in Python è la seguente:

#Caso semplice con un if quindi se il valore è minore o uguale a 18 non fa niente
#Come si può notare non c'è bisogno di parentesi tonde intorno alla condizione 
#o anche di parentesi graffe per delimitare il blocco di codice anzi in Python l'indentazione è fondamentale per definire i blocchi di codice
anni=int(input("Quanti anni hai? "))
if anni>=18:
    print("Sei maggiorenne.")

#Caso con if ed else quindi se il valore è minore o uguale a 18 stampa che è minorenne
if anni>=18:
    print("Sei maggiorenne.")
else:
    print("Sei minorenne.")

#Caso con if, elif ed else quindi se il valore è minore di 18 stampa che è minorenne
#se il valore è uguale a 18 stampa che ha appena raggiunto la maggiore età
#se il valore è maggiore di 18 stampa che è maggiorenne
if anni<18:
    print("Sei minorenne.")
elif anni==18:# -> elif sarebbe un se alternativo sarebbe come fare un if nidificato dentro un else solo in modo più carino (se abbiamo molti casi specifici usare switch)
    print("Hai appena raggiunto la maggiore età.")
else:
    print("Sei maggiorenne.")

if anni<0:
    print("Errore: l'età non può essere negativa.")
elif anni<18:
    print("Sei minorenne.")
elif anni==18:
    print("Hai appena raggiunto la maggiore età.")
else:
    print("Sei maggiorenne.")
    
#Possiamo anche annidare più if dentro altri if per creare condizioni più complesse
if anni>=0:
    if anni<18:
        print("Sei minorenne.")
    elif anni==18:
        print("Hai appena raggiunto la maggiore età.")
    else:
        print("Sei maggiorenne.")
else:
    print("Errore: l'età non può essere negativa.")
#Tuttavia è importante non esagerare con l'annidamento degli if per mantenere il codice leggibile e comprensibile.