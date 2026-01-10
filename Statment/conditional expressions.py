#Sono i Ternary Operators o Conditional Expressions e permettono di scrivere un'istruzione if-else in una singola riga.
#La sintassi generale di un'operazione condizionale è la seguente:
# valore_se_vero if condizione else valore_se_falso

numero=int(input("Inserisci un numero: "))
print("Positivo" if numero>=0 else "Negativo")

numeroPN=True if numero>=0 else False
print(f"Il numero è positivo? {numeroPN}")