#Sono i Ternary Operators o Conditional Expressions e permettono di scrivere un'istruzione if-else in una singola riga.
#La sintassi generale di un'operazione condizionale è la seguente:
# valore_se_vero if condizione else valore_se_falso

numero=int(input("Inserisci un numero: "))
print("Positivo" if numero>=0 else "Negativo")

numero1="Positivo" if numero>=0 else "Negativo"
print(f"Il numero {numero} è {numero1}.")

#Esempio per trovare il massimo e il minimo tra due numeri
#Input dei numeri
a=int(input("Inserisci il primo numero: "))
b=int(input("Inserisci il secondo numero: "))

#Confronto
massimo=a if a>b else b
minimo=b if a>b else a

#Stampa i risultati
print(f"Il massimo tra {a} e {b} è {massimo}.")
print(f"Il minimo tra {a} e {b} è {minimo}.")